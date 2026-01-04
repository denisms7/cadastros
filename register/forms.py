from django import forms
from .models import Register, PessoaFisica, PessoaJuridica
from django.core.exceptions import ValidationError
from .utils import cpf_validate, cnpj_validate, get_bank


class Pj_ModelForm(forms.ModelForm):
    bank = forms.ChoiceField(choices=get_bank(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['legal'].required = True
        self.fields['fantasy'].required = True
        self.fields['cnpj'].required = True

    class Meta:
        model = PessoaJuridica
        fields = [
            'active',
            'legal',
            'fantasy',
            'cnpj',
            'cnpj_situation',
            'cnpj_carrying',
            'cnpj_date',
            'cnpj_type_activity',
            'cnpj_activity',
            'n_state',
            'n_municipal',
            'obs',
            'email_1',
            'email_2',
            'phone_1',
            'phone_1_type',
            'phone_2',
            'phone_2_type',
            'phone_3',
            'phone_3_type',
            'link_1',
            'link_2',
            'obs_contact',
            'cep',
            'state',
            'city',
            'neighborhood',
            'address',
            'number',
            'complement',
            'obs_address',
            'title_holder',
            'document_type',
            'document_holder',
            'account_type',
            'bank',
            'agency',
            'account',
            'digit',
            'pix_1',
            'pix_2',
            'obs_bank',
        ]
        widgets = {
            'cnpj_date': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj:
            cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
            if not cnpj_validate(cnpj):
                raise ValidationError('CNPJ Inválido')

            # Verifica se já existe outro registro com este CNPJ
            existing = PessoaJuridica.objects.filter(cnpj=cnpj).exclude(pk=self.instance.pk if self.instance.pk else None)
            if existing.exists():
                raise ValidationError('Cadastro com este CNPJ já existe.')

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

    def clean_bank(self):
        bank = self.cleaned_data.get('bank')
        if bank is not None:
            try:
                return int(bank)
            except ValueError:
                raise ValidationError("Número do banco inválido.")
        return bank


class Pf_ModelForm(forms.ModelForm):
    bank = forms.ChoiceField(choices=get_bank(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['last_name'].required = True
        self.fields['cpf'].required = True
        self.fields['sex'].required = True

    class Meta:
        model = PessoaFisica
        fields = [
            'active',
            'name',
            'last_name',
            'cpf',
            'rg',
            'rg_issuer',
            'rg_expedition',
            'birth',
            'education',
            'sex',
            'spouse_status',
            'spouse_name',
            'spouse_last_name',
            'mother_name',
            'mother_last_name',
            'father_name',
            'father_last_name',
            'obs',
            'email_1',
            'email_2',
            'phone_1',
            'phone_1_type',
            'phone_2',
            'phone_2_type',
            'phone_3',
            'phone_3_type',
            'link_1',
            'link_2',
            'obs_contact',
            'cep',
            'state',
            'city',
            'neighborhood',
            'address',
            'number',
            'complement',
            'obs_address',
            'title_holder',
            'document_type',
            'document_holder',
            'account_type',
            'bank',
            'agency',
            'account',
            'digit',
            'pix_1',
            'pix_2',
            'obs_bank',
            'cnh_n',
            'cnh_emission',
            'cnh_validity',
            'cnh_category',
        ]
        widgets = {
            'rg_expedition': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'birth': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'cnh_emission': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'cnh_validity': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf = cpf.replace('.', '').replace('-', '')
            if not cpf_validate(cpf):
                raise ValidationError('CPF Inválido')

            # Verifica se já existe outro registro com este CPF
            existing = PessoaFisica.objects.filter(cpf=cpf).exclude(pk=self.instance.pk if self.instance.pk else None)
            if existing.exists():
                raise ValidationError('Cadastro com este CPF já existe.')

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

    def clean_bank(self):
        bank = self.cleaned_data.get('bank')
        if bank is not None:
            try:
                return int(bank)
            except ValueError:
                raise ValidationError("Número do banco inválido.")
        return bank


class Detail_ModelForm(forms.ModelForm):
    bank = forms.ChoiceField(choices=get_bank(), required=False)

    class Meta:
        model = Register
        fields = "__all__"
        widgets = {
            'rg_expedition': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'birth': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'cnh_emission': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'cnh_validity': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
            'cnpj_date': forms.DateInput(format=("%Y-%m-%d"), attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = True
