from django import forms
from .models import Cadastro
from django.core.exceptions import ValidationError
from cadastros.utils import cpf_validate, cnpj_validate, get_bank


class Pj_ModelForm(forms.ModelForm):
    n_banco = forms.ChoiceField(choices=get_bank(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pessoa_juridica'].required = True
        self.fields['nome_fantasia'].required = True
        self.fields['cnpj'].required = True

    class Meta:
        model = Cadastro
        fields = [
            'status',
            'pessoa_juridica',
            'nome_fantasia',
            'cnpj',
            'cnpj_situacao',
            'cnpj_porte',
            'cnpj_data_abertura',
            'cnpj_tipo',
            'cnpj_atividade_principal',
            'is_estadual',
            'is_municipal',
            'email_1',
            'email_2',
            'fone_1',
            'fone_1_tipo',
            'fone_2',
            'fone_2_tipo',
            'fone_3',
            'fone_3_tipo',
            'link_1',
            'link_2',
            'obs_contato',
            'cep',
            'estado',
            'cidade',
            'bairro',
            'endereco',
            'numero',
            'complemento',
            'obs_endereco',
            'nome_razao_titular',
            'tipo_de_documento',
            'documento_titular',
            'tipo_de_conta',
            'n_banco',
            'agencia',
            'conta',
            'digito',
            'pix_1',
            'pix_2',
            'obs_banco',
        ]
        widgets = {
            'cnpj_data_abertura': forms.DateInput(format=("%Y-%m-%d")),
            'rg_expedicao': forms.DateInput(format=("%Y-%m-%d")),
            'nascimento': forms.DateInput(format=("%Y-%m-%d")),
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj:
            cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
            if not cnpj_validate(cnpj):
                raise ValidationError('CNPJ Inválido')
            return cnpj
        return cnpj

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if cep:
            cep = cep.replace('.', '').replace('-', '')
            if len(cep) != 8:
                raise ValidationError('CEP Inválido')
            return cep
        return cep

    def clean_n_banco(self):
        n_banco = self.cleaned_data.get('n_banco')
        if n_banco is not None:
            try:
                return int(n_banco)
            except ValueError:
                raise ValidationError("Número do banco inválido.")
        return n_banco


class Pf_ModelForm(forms.ModelForm):
    n_banco = forms.ChoiceField(choices=get_bank(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['primeiro_nome'].required = True
        self.fields['ultimo_nome'].required = True
        self.fields['cpf'].required = True
        self.fields['sexo'].required = True

    class Meta:
        model = Cadastro
        fields = [
            'status',
            'primeiro_nome',
            'ultimo_nome',
            'cpf',
            'rg',
            'rg_emissor',
            'rg_expedicao',
            'nascimento',
            'escolaridade',
            'sexo',
            'estado_civil',
            'conjuge_primeiro_nome',
            'conjuge_ultimo_nome',
            'mae_primeiro_nome',
            'mae_ultimo_nome',
            'pai_primeiro_nome',
            'pai_ultimo_nome',
            'obs_pessoal',
            'email_1',
            'email_2',
            'fone_1',
            'fone_1_tipo',
            'fone_2',
            'fone_2_tipo',
            'fone_3',
            'fone_3_tipo',
            'link_1',
            'link_2',
            'obs_contato',
            'cep',
            'estado',
            'cidade',
            'bairro',
            'endereco',
            'numero',
            'complemento',
            'obs_endereco',
            'nome_razao_titular',
            'tipo_de_documento',
            'documento_titular',
            'tipo_de_conta',
            'n_banco',
            'agencia',
            'conta',
            'digito',
            'pix_1',
            'pix_2',
            'obs_banco',
            'cnh_n',
            'cnh_emissao',
            'cnh_validade',
            'cnh_categoria',
        ]
        widgets = {
            'rg_expedicao': forms.DateInput(format=("%Y-%m-%d")),
            'nascimento': forms.DateInput(format=("%Y-%m-%d")),
            'cnh_emissao': forms.DateInput(format=("%Y-%m-%d")),
            'cnh_validade': forms.DateInput(format=("%Y-%m-%d")),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf = cpf.replace('.', '').replace('-', '')
            if not cpf_validate(cpf):
                raise ValidationError('CPF Inválido')
            return cpf
        return cpf

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if cep:
            cep = cep.replace('.', '').replace('-', '')
            if len(cep) != 8:
                raise ValidationError('CEP Inválido')
            return cep
        return cep

    def clean_n_banco(self):
        n_banco = self.cleaned_data.get('n_banco')
        if n_banco is not None:
            try:
                return int(n_banco)
            except ValueError:
                raise ValidationError("Número do banco inválido.")
        return n_banco


class Detail_ModelForm(forms.ModelForm):
    n_banco = forms.ChoiceField(choices=get_bank(), required=False)

    class Meta:
        model = Cadastro
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = True
