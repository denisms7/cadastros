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

from .models import Cadastro_Pessoa, Cadastro_Empresa
from .forms import FormCadastroPessoa, FormCadastroEmpresa

from datetime import datetime


from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

class BuscaPessoa(LoginRequiredMixin, ListView):
    paginate_by = 20
    model = Cadastro_Pessoa
    template_name = 'cadastros/pessoa/busca_pessoa.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=query) | Q(cpf__icontains=query) | Q(ultimo_nome__icontains=query)
            )
        return queryset


class CadastroPessoa(LoginRequiredMixin, CreateView):
    model = Cadastro_Pessoa
    form_class = FormCadastroPessoa
    template_name = 'cadastros/pessoa/cadastro_pessoa.html'
    success_url = reverse_lazy('pessoa-busca')

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


class EditarPessoa(LoginRequiredMixin, UpdateView):
    model = Cadastro_Pessoa
    form_class = FormCadastroPessoa
    template_name = 'cadastros/pessoa/cadastro_pessoa.html'
    success_url = reverse_lazy('pessoa-busca')

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


# Cadastro_Pessoa delete
@user_passes_test(lambda user: user.is_authenticated)
def DeletePessoa(request, pk):
    try:
        registro = Cadastro_Pessoa.objects.get(id=pk)
        registro.delete()
        messages.success(request, 'Cadastro deletado')
        return redirect('pessoa-busca')
    except:
        messages.warning(request, 'Não é possível deletar este registro')
        return redirect('pessoa-busca')




# EMPRESA =====================================================================================================
class BuscaEmpresa(LoginRequiredMixin, ListView):
    paginate_by = 20
    model = Cadastro_Empresa
    template_name = 'cadastros/empresa/busca_empresa.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nome_fantasia__icontains=query) | Q(cnpj__icontains=query) | Q(pessoa_juridica__icontains=query)
            )
        return queryset


class CadastroEmpresa(LoginRequiredMixin, CreateView):
    model = Cadastro_Empresa
    form_class = FormCadastroEmpresa
    template_name = 'cadastros/empresa/cadastro_empresa.html'
    success_url = reverse_lazy('empresa-busca')

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


class EditarEmpresa(LoginRequiredMixin, UpdateView):
    model = Cadastro_Empresa
    form_class = FormCadastroEmpresa
    template_name = 'cadastros/empresa/cadastro_empresa.html'
    success_url = reverse_lazy('empresa-busca')

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


# Cadastro_Empresa delete
@user_passes_test(lambda user: user.is_authenticated)
def DeleteEmpresa(request, pk):
    try:
        registro = Cadastro_Empresa.objects.get(id=pk)
        registro.delete()
        messages.success(request, 'Cadastro deletado')
        return redirect('empresa-busca')
    except:
        messages.warning(request, 'Não é possível deletar este registro')
        return redirect('empresa-busca')


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
