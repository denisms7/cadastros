from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from django.contrib import messages
from .models import Cadastro
from django.db.models import Q
from django.db import IntegrityError
from .forms import FormCadastroPessoa, FormCadastroEmpresa
from django.core.paginator import Paginator
from cadastros.utils import cpf_validate, cnpj_validate


class Agenda(LoginRequiredMixin, ListView):
    model = Cadastro
    template_name = 'cadastros/agenda.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=query) | Q(ultimo_nome__icontains=query) | Q(nome_fantasia__icontains=query) | Q(ultimo_nome__icontains=query)
            )
        return queryset


class BuscaPessoa(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 20
    model = Cadastro
    template_name = 'cadastros/pessoa/busca_pessoa.html'
    permission_required = 'cadastros.view_cadastro'

    def get_queryset(self):
        queryset = super().get_queryset().filter(tipo=0)  # Filtra apenas tipo=0
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=query) | Q(cpf__icontains=query) | Q(ultimo_nome__icontains=query)
            )
        return queryset


class CadastroPessoa(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Cadastro
    form_class = FormCadastroPessoa
    template_name = 'cadastros/pessoa/cadastro_pessoa.html'
    success_url = reverse_lazy('pessoa-busca')
    permission_required = 'cadastros.add_cadastro'

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        if len(cpf) > 1:
            cpf = cpf.replace('.', '').replace('-', '')
            form.instance.cpf = cpf

        cep = form.cleaned_data.get('cep')
        if cep is not None:
            form.instance.cep = cep.replace('.', '').replace('-', '')

        if not cpf_validate(cpf):
            messages.warning(self.request, f"O CPF {cpf} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.tipo = 0
        form.instance.cadastrado_por = self.request.user
        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

    def handle_unique(self, e):
        if "cpf" in str(e):
            messages.warning(self.request, "Cadastro com CPF Duplicado. o registro nao foi salvo")
        else:
            messages.warning(self.request, "Erro. Salvamento cancelado")
        return self.form_invalid(self.get_form())


class EditarPessoa(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Cadastro
    form_class = FormCadastroPessoa
    template_name = 'cadastros/pessoa/cadastro_pessoa.html'
    success_url = reverse_lazy('pessoa-busca')
    permission_required = 'cadastros.change_cadastro'

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        if cpf is not None:
            form.instance.cpf = cpf.replace('.', '').replace('-', '')

        cep = form.cleaned_data.get('cep')
        if cep is not None:
            form.instance.cep = cep.replace('.', '').replace('-', '')

        if not cpf_validate(cpf):
            messages.warning(self.request, f"O CPF {cpf} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

    def handle_unique(self, e):
        if "cpf" in str(e):
            messages.warning(self.request, "Cadastro com CPF Duplicado. o registro nao foi salvo")
        else:
            messages.warning(self.request, "Erro. Salvamento cancelado")
        return self.form_invalid(self.get_form())


# EMPRESA =====================================================================================================
class BuscaEmpresa(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 20
    model = Cadastro
    template_name = 'cadastros/empresa/busca_empresa.html'
    permission_required = 'cadastros.view_cadastro'

    def get_queryset(self):
        queryset = super().get_queryset().filter(tipo=1)  # Filtra apenas empresas
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nome_fantasia__icontains=query) | Q(cnpj__icontains=query) | Q(pessoa_juridica__icontains=query)
            )
        return queryset


class CadastroEmpresa(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Cadastro
    form_class = FormCadastroEmpresa
    template_name = 'cadastros/empresa/cadastro_empresa.html'
    success_url = reverse_lazy('empresa-busca')
    permission_required = 'cadastros.add_cadastro'

    def form_valid(self, form):
        cnpj = form.cleaned_data.get('cnpj')
        cep = form.cleaned_data.get('cep')
        if cnpj:
            cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
            form.instance.cnpj = cnpj
            if not cnpj_validate(cnpj):
                messages.warning(self.request, f"O CNPJ {cnpj} é inválido, O registro não foi salvo.")
                return self.form_invalid(form)
        if cep:
            form.instance.cep = cep.replace('.', '').replace('-', '')

        form.instance.tipo = 1
        form.instance.cadastrado_por = self.request.user
        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

    def handle_unique(self, e):
        if "cnpj" in str(e):
            messages.warning(self.request, "Cadastro com CNPJ duplicado. O registro não foi salvo.")
        else:
            messages.warning(self.request, "Erro. Salvamento cancelado.")
        return self.form_invalid(self.get_form())


class EditarEmpresa(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Cadastro
    form_class = FormCadastroEmpresa
    template_name = 'cadastros/empresa/cadastro_empresa.html'
    success_url = reverse_lazy('empresa-busca')
    permission_required = 'cadastros.change_cadastro'

    def form_valid(self, form):
        cnpj = form.cleaned_data.get('cnpj')
        cep = form.cleaned_data.get('cep')
        if cnpj:
            cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
            form.instance.cnpj = cnpj
            if not cnpj_validate(cnpj):
                messages.warning(self.request, f"O CNPJ {cnpj} é inválido, O registro não foi salvo.")
                return self.form_invalid(form)
        if cep:
            form.instance.cep = cep.replace('.', '').replace('-', '')

        if not cnpj_validate(cnpj):
            messages.warning(self.request, f"O CNPJ {cnpj} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        url = super().form_valid(form)
        messages.success(self.request, "Registro alterado com sucesso.")
        return url


# Delete Empresa
class EmpresaDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy("empresa-busca")

    def post(self, request, pk, *args, **kwargs):
        registro = get_object_or_404(Cadastro, id=pk)
        try:
            registro.delete()
            messages.success(request, "Cadastro deletado")
        except Exception:
            messages.warning(request, "Não é possível deletar este registro")
        return redirect(self.success_url)


# Delete Pessoa
class PessoaDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy("pessoa-busca")

    def post(self, request, pk, *args, **kwargs):
        registro = get_object_or_404(Cadastro, id=pk)
        try:
            registro.delete()
            messages.success(request, "Cadastro deletado")
        except Exception:
            messages.warning(request, "Não é possível deletar este registro")
        return redirect(self.success_url)


@user_passes_test(lambda user: user.is_authenticated)
def cadastro_historico(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    historico = list(cadastro.history.all().order_by('-history_date'))
    paginate_by = 20

    historico_com_diffs = []
    for i, item in enumerate(historico):
        diff_verbose = None
        if i + 1 < len(historico):
            previous = historico[i + 1]
            try:
                diff_obj = item.diff_against(previous)
                # Monta uma lista com verbose_name, old e new
                diff_verbose = []
                for change in diff_obj.changes:
                    field_name = change.field
                    try:
                        verbose_name = cadastro._meta.get_field(field_name).verbose_name
                    except Exception:
                        verbose_name = field_name  # fallback caso o campo não exista mais
                    diff_verbose.append({
                        'field': field_name,
                        'verbose_name': verbose_name,
                        'old': change.old,
                        'new': change.new
                    })
            except AttributeError:
                diff_verbose = None

        historico_com_diffs.append({'item': item, 'diff': diff_verbose})

    paginator = Paginator(historico_com_diffs, paginate_by)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'cadastros/historico.html', {
        'cadastro': cadastro,
        'page_obj': page_obj,
    })
