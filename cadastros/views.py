from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from itertools import cycle
from django.shortcuts import redirect

from .models import Cadastro_Pessoa
from .forms import FormCadastro

from datetime import datetime

class BuscaPessoa(ListView):
    paginate_by = 20
    model = Cadastro_Pessoa
    template_name = 'cadastro_pessoa/busca_pessoa.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=query) | Q(cpf__icontains=query) | Q(ultimo_nome__icontains=query)
            )
        return queryset


class CadastroPessoa(CreateView):
    model = Cadastro_Pessoa
    form_class = FormCadastro
    template_name = 'cadastro_pessoa/cadastro_pessoa.html'
    success_url = reverse_lazy('pessoa-busca')

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        if not cpf_validate(cpf):
            messages.warning(self.request, f"O CPF {cpf} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.cadastrado_por = self.request.user
        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        url = super().form_valid(form)
        messages.success(self.request, "Registro salvo com sucesso.")
        return url


class EditarPessoa(UpdateView):
    model = Cadastro_Pessoa
    form_class = FormCadastro
    template_name = 'cadastro_pessoa/cadastro_pessoa.html'
    success_url = reverse_lazy('pessoa-busca')

    def form_valid(self, form):
        cpf = form.cleaned_data.get('cpf')
        if not cpf_validate(cpf):
            messages.warning(self.request, f"O CPF {cpf} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()
        
        url = super().form_valid(form)
        messages.success(self.request, "Registro alterado com sucesso.")
        return url


class DeletePessoa(DeleteView):
    model = Cadastro_Pessoa
    success_url = reverse_lazy('pessoa-busca')
    template_name = 'cadastro_pessoa/delete_pessoa.html'

    def form_valid(self, form):
        try:
            url = super().form_valid(form)
            messages.success(self.request, "Registro Deletado com sucesso.")
            return url
        except:
            messages.warning(self.request, "Não foi possivel deletar o registro")
            return redirect('pessoa-busca')



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

# EMPRESA


class BuscaEmpresa(ListView):
    paginate_by = 20
    model = Cadastro_Empresa
    template_name = 'cadastro_empresa/busca_empresa.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nome_fantasia__icontains=query) | Q(cnpj__icontains=query) | Q(pessoa_juridica__icontains=query)
            )
        return queryset


class CadastroEmpresa(CreateView):
    model = Cadastro_Empresa
    form_class = FormCadastro
    template_name = 'cadastro_empresa/cadastro_empresa.html'
    success_url = reverse_lazy('empresa-busca')

    def form_valid(self, form):
        cnpj = form.cleaned_data.get('cnpj')
        if not cnpj_validate(cnpj):
            messages.warning(self.request, f"O CNPJ {cnpj} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.cadastrado_por = self.request.user
        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        url = super().form_valid(form)
        messages.success(self.request, "Registro salvo com sucesso.")
        return url


class EditarEmpresa(UpdateView):
    model = Cadastro_Empresa
    form_class = FormCadastro
    template_name = 'cadastro_empresa/cadastro_empresa.html'
    success_url = reverse_lazy('empresa-busca')

    def form_valid(self, form):
        cnpj = form.cleaned_data.get('cnpj')
        if not cnpj_validate(cnpj):
            messages.warning(self.request, f"O CNPJ {cnpj} é inválido, O registro não foi salvo.")
            return self.form_invalid(form)

        form.instance.ultima_att = self.request.user.username
        form.instance.data_att = datetime.now()

        url = super().form_valid(form)
        messages.success(self.request, "Registro alterado com sucesso.")
        return url


class DeleteEmpresa(DeleteView):
    model = Cadastro_Empresa
    success_url = reverse_lazy('empresa-busca')
    template_name = 'cadastro_empresa/delete_empresa.html'

    def form_valid(self, form):
        try:
            url = super().form_valid(form)
            messages.success(self.request, "Registro Deletado com sucesso.")
            return url
        except:
            messages.warning(self.request, "Não foi possivel deletar o registro")
            return redirect('pessoa-busca')


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
