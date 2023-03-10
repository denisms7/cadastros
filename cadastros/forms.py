from django import forms
from .models import Cadastro_Empresa, Cadastro_Pessoa

class FormCadastroEmpresa(forms.ModelForm):
    class Meta:
        model = Cadastro_Empresa
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
        ]
        widgets = {
            'cnpj_data_abertura': forms.DateInput(format=("%Y-%m-%d")),
            'rg_expedicao': forms.DateInput(format=("%Y-%m-%d")),
            'nascimento': forms.DateInput(format=("%Y-%m-%d")),
        }

class FormCadastroPessoa(forms.ModelForm):
    class Meta:
        model = Cadastro_Pessoa
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
        ]
        widgets = {
            'rg_expedicao': forms.DateInput(format=("%Y-%m-%d")),
            'nascimento': forms.DateInput(format=("%Y-%m-%d")),
        }
