from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q
# from django.core.paginator import Paginator
from itertools import cycle
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST

from .models import Cadastro
from .forms import FormCadastroPessoa, FormCadastroEmpresa

from datetime import datetime

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404

from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info ',
}

# messages.add_message(request, constants.ERROR, 'Preencha todos os campos')

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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
                Q(primeiro_nome__icontains=query) |
                Q(cpf__icontains=query) |
                Q(ultimo_nome__icontains=query)
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
        if cep != None:
            cep = cep.replace('.', '').replace('-', '')
            form.instance.cep = cep 

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
        if cpf != None:
            cpf = cpf.replace('.', '').replace('-', '')
            form.instance.cpf = cpf 

        cep = form.cleaned_data.get('cep')
        if cep != None:
            cep = cep.replace('.', '').replace('-', '')
            form.instance.cep = cep 
        
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
                Q(nome_fantasia__icontains=query) |
                Q(cnpj__icontains=query) |
                Q(pessoa_juridica__icontains=query)
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
            cep = cep.replace('.', '').replace('-', '')
            form.instance.cep = cep 

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
            cep = cep.replace('.', '').replace('-', '')
            form.instance.cep = cep 

        if not cnpj_validate(cnpj):
            messages.warning(self.request, f"O CNPJ {cnpj} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        url = super().form_valid(form)
        messages.success(self.request, "Registro alterado com sucesso.")
        return url

# Delete Empresa
@csrf_protect
@require_POST
@user_passes_test(lambda user: user.is_authenticated)
def DeleteEmpresa(request, pk):
    registro = get_object_or_404(Cadastro, id=pk)
    try:
        registro.delete()
        messages.success(request, 'Cadastro deletado')
    except:
        messages.warning(request, 'Não é possível deletar este registro')
    return redirect('empresa-busca')

# Delete Pessoa
@csrf_protect
@require_POST
@user_passes_test(lambda user: user.is_authenticated)
def DeletePessoa(request, pk):
    try:
        registro = Cadastro.objects.get(id=pk)
        registro.delete()
        messages.success(request, 'Cadastro deletado')
        return redirect('pessoa-busca')
    except:
        messages.warning(request, 'Não é possível deletar este registro')
        return redirect('pessoa-busca')

from django.core.paginator import Paginator

@csrf_protect
def cadastro_historico(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    historico = list(cadastro.history.all().order_by('-history_date'))
    paginate_by = 20

    historico_com_diffs = []
    for i, item in enumerate(historico):
        diff = None
        if i + 1 < len(historico):
            previous = historico[i + 1]
            try:
                diff = item.diff_against(previous)
            except AttributeError:
                diff = None
        historico_com_diffs.append({'item': item, 'diff': diff})

    paginator = Paginator(historico_com_diffs, paginate_by)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'cadastros/historico.html', {
        'cadastro': cadastro,
        'page_obj': page_obj,
    })






def cpf_validate(cpf: str) -> bool:
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return False
    if not cpf.isdigit():
        return False
    if cpf in (c * TAMANHO_CPF for c in "1234567890"):
        return False
    cpf_reverso = cpf[::-1]
    for i in range(2, 0, -1):
        cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
        dv_calculado = sum(map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
        if cpf_reverso[i - 1:i] != str(dv_calculado % 10):
            return False
    return True
    

def cnpj_validate(cnpj: str) -> bool:
    LENGTH_CNPJ = 14
    if len(cnpj) != LENGTH_CNPJ:
        return False
    if not cnpj.isdigit():
        return False
    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return False
    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False
    return True

class Agenda(LoginRequiredMixin, ListView):
    model = Cadastro 
    template_name = 'cadastros/agenda.html'
    paginate_by = 20
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=query) | Q(ultimo_nome__icontains=query) | 
                Q(nome_fantasia__icontains=query) | Q(ultimo_nome__icontains=query)
            )
        return queryset
    

