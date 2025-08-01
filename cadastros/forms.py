from django import forms
from .models import Cadastro
import requests


def get_bancos_choices():
    url = 'https://brasilapi.com.br/api/banks/v1'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except (requests.exceptions.RequestException, ValueError):
        raise print('Erro ao buscar bancos.')
    else:
        bancos = [(bank['code'], f"{bank['code']} - {bank['name']}") for bank in data if bank['code']]
        bancos.sort()
        return [(0,'---------')] + bancos

class FormCadastroEmpresa(forms.ModelForm):
    n_banco = forms.ChoiceField(choices=get_bancos_choices(), required=False)

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
            'ultima_att',
            'data_att',

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

        def clean(self):
            cleaned_data = super().clean()
            n_banco = cleaned_data.get('n_banco')
            if n_banco is not None:
                cleaned_data['n_banco'] = int(n_banco)
            return cleaned_data

class FormCadastroPessoa(forms.ModelForm):
    n_banco = forms.ChoiceField(choices=get_bancos_choices(), required=False)


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
            'ultima_att',
            'data_att',
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

    def clean(self):
        cleaned_data = super().clean()
        n_banco = cleaned_data.get('n_banco')

        if n_banco is not None:
            cleaned_data['n_banco'] = int(n_banco)

        return cleaned_data
