from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

ACTIVE_CHOICES = [
    (True, _('Ativo')),
    (False, _('Inativo')),
]


class Register(models.Model):
    SEXO_CHOICES = [
        ('M', _('Homem cisgênero')),
        ('MT', _('Homem transgênero')),
        ('F', _('Mulher cisgênero')),
        ('FT', _('Mulher transgênero')),
        ('NF', _('Pessoa não binária do sexo feminino')),
        ('NM', _('Pessoa não binária do sexo masculino')),
        ('-', _('Não informado')),
    ]

    ESCOLARIDADE_CHOICES = [
        (1, _('Sem Ensino')),
        (2, _('Fundamental - Incompleto')),
        (3, _('Fundamental - Completo')),
        (4, _('Médio - Incompleto')),
        (5, _('Médio - Completo')),
        (6, _('Superior - Incompleto')),
        (7, _('Superior - Completo')),
        (8, _('Pós-graduação (Lato senso) - Incompleto')),
        (9, _('Pós-graduação (Lato senso) - Completo')),
        (10, _('Pós-graduação (Stricto sensu, nível mestrado) - Incompleto')),
        (11, _('Pós-graduação (Stricto sensu, nível mestrado) - Completo')),
        (12, _('Pós-graduação (Stricto sensu, nível doutor) - Incompleto')),
        (13, _('Pós-graduação (Stricto sensu, nível doutor) - Completo')),
    ]

    ESTADO_CIVIL_CHOICES = [
        (1, _('Casado')),
        (2, _('Divorciado')),
        (3, _('Solteiro')),
        (4, _('União Estavel')),
        (5, _('Viúvo')),
    ]

    CONTATOS_CHOICES = [
        (1, _('Telefone')),
        (2, _('WhatsApp')),
    ]

    CONTA_TIPO_CHOICES = [
        (1, _('Conta Corrente')),
        (2, _('Conta Salário')),
        (3, _('Conta Poupança')),
    ]

    TIPO_DOCUMENTO_CHOICES = [
        (0, 'CPF'),
        (1, 'CNPJ'),
    ]

    CHOICES_CNH = [
        ('ACC', 'ACC'),
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    TYPE_CHOICES = [
        (0, _('Pessoa Física')),
        (1, _('Pessoa Jurídica')),
    ]

    # Sistema
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, verbose_name=_('Tipo'), default=None)
    active = models.BooleanField(choices=ACTIVE_CHOICES, verbose_name=_('Ativo'), default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Cadastro'))
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Cadastrado'))
    # Dados da Empresa
    legal = models.CharField(max_length=200, verbose_name=_('Razão Social'), null=True, blank=True)
    fantasy = models.CharField(max_length=200, verbose_name=_('Nome Fantasia'), null=True, blank=True)
    n_state = models.CharField(max_length=14, verbose_name=_('Incrição Estadual'), null=True, blank=True)
    n_municipal = models.CharField(max_length=14, verbose_name=_('Incrição Municipal'), null=True, blank=True)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name=_('CNPJ'), null=True, blank=True)
    cnpj_situation = models.CharField(max_length=200, verbose_name=_('Situação'), null=True, blank=True)
    cnpj_carrying = models.CharField(max_length=200, verbose_name=_('Porte de Empresa'), null=True, blank=True)
    cnpj_date = models.DateField(verbose_name=_('Data de Abertura'), null=True, blank=True)
    cnpj_type_activity = models.CharField(max_length=200, verbose_name=_('Tipo'), null=True, blank=True)
    cnpj_activity = models.TextField(max_length=2000, verbose_name=_('Atividade Principal'), null=True, blank=True)
    # Dados Pessoais
    name = models.CharField(max_length=50, verbose_name=_('Nome'), null=True, blank=True)
    last_name = models.CharField(max_length=150, verbose_name=_('Sobrenome'), null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name=_('CPF'), null=True, blank=True)
    rg = models.CharField(max_length=11, verbose_name=_('RG (Descontinuado)'), null=True, blank=True)
    rg_issuer = models.CharField(max_length=3, verbose_name=_('Emissor'), null=True, blank=True)
    rg_expedition = models.DateField(verbose_name=_('Expedicao'), null=True, blank=True)
    birth = models.DateField(verbose_name=_('Nascimento'), null=True, blank=True)
    education = models.PositiveSmallIntegerField(choices=ESCOLARIDADE_CHOICES, verbose_name=_('Escolaridade'), null=True, blank=True)
    sex = models.CharField(max_length=2, choices=SEXO_CHOICES, verbose_name=_('Sexo'), null=True, blank=True)
    # Conjuge
    spouse_status = models.PositiveSmallIntegerField(choices=ESTADO_CIVIL_CHOICES, verbose_name=_('Estado Civil'), null=True, blank=True)
    spouse_name = models.CharField(max_length=50, verbose_name=_('Nome do Conjuge'), null=True, blank=True)
    spouse_last_name = models.CharField(max_length=150, verbose_name=_('Sobrenome do Conjuge'), null=True, blank=True)
    # Pais
    mother_name = models.CharField(max_length=50, verbose_name=_('Nome da Mãe'), null=True, blank=True)
    mother_last_name = models.CharField(max_length=150, verbose_name=_('Sobrenome da Mãe'), null=True, blank=True)
    father_name = models.CharField(max_length=50, verbose_name=_('Nome do Pai'), null=True, blank=True)
    father_last_name = models.CharField(max_length=150, verbose_name=_('Sobrenome do Pai'), null=True, blank=True)
    obs = models.TextField(max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # CNH
    cnh_n = models.CharField(max_length=50, verbose_name=_('CNH'), null=True, blank=True)
    cnh_emission = models.DateField(verbose_name=_('Emissão'), null=True, blank=True)
    cnh_validity = models.DateField(verbose_name=_('Validade'), null=True, blank=True)
    cnh_category = models.CharField(max_length=5, choices=CHOICES_CNH, verbose_name=_('Categoria'), null=True, blank=True)
    # Contato
    email_1 = models.EmailField(max_length=150, verbose_name=_('E-mail'), null=True, blank=True)
    email_2 = models.EmailField(max_length=150, verbose_name=_('E-mail'), null=True, blank=True)
    phone_1 = models.CharField(max_length=15, verbose_name=_('Contato'), null=True, blank=True)
    phone_1_type = models.PositiveSmallIntegerField(choices=CONTATOS_CHOICES, null=True, blank=True)
    phone_2 = models.CharField(max_length=15, verbose_name=_('Contato'), null=True, blank=True)
    phone_2_type = models.PositiveSmallIntegerField(choices=CONTATOS_CHOICES, null=True, blank=True)
    phone_3 = models.CharField(max_length=15, verbose_name=_('Contato'), null=True, blank=True)
    phone_3_type = models.PositiveSmallIntegerField(choices=CONTATOS_CHOICES, null=True, blank=True)
    link_1 = models.URLField(verbose_name=_('Link'), null=True, blank=True)
    link_2 = models.URLField(verbose_name=_('Link'), null=True, blank=True)
    obs_contact = models.TextField(max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # Endereço
    cep = models.CharField(max_length=10, verbose_name='CEP', null=True, blank=True)
    state = models.CharField(max_length=2, verbose_name=_('Estado'), null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name=_('Cidade'), null=True, blank=True)
    neighborhood = models.CharField(max_length=200, verbose_name=_('Bairro'), null=True, blank=True)
    address = models.CharField(max_length=250, verbose_name=_('Endereço'), null=True, blank=True)
    number = models.IntegerField(default=0, verbose_name=_('Número'), null=True, blank=True)
    complement = models.CharField(max_length=250, verbose_name=_('Complemento'), null=True, blank=True)
    obs_address = models.TextField(max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # Banco
    title_holder = models.CharField(max_length=50, verbose_name=_('Nome/Razão'), null=True, blank=True)
    document_type = models.PositiveSmallIntegerField(choices=TIPO_DOCUMENTO_CHOICES, verbose_name=_('Tipo de Documento'), null=True, blank=True)
    document_holder = models.CharField(max_length=18, verbose_name=_('CPF/CNPJ'), null=True, blank=True)
    account_type = models.PositiveSmallIntegerField(choices=CONTA_TIPO_CHOICES, verbose_name=_('Tipo de Conta'), null=True, blank=True)

    bank = models.IntegerField(default=0, verbose_name=_('N° Banco'), null=True, blank=True)
    agency = models.CharField(max_length=10, verbose_name=_('Agencia'), null=True, blank=True)
    account = models.CharField(max_length=50, verbose_name=_('N° Conta'), null=True, blank=True)
    digit = models.CharField(max_length=5, verbose_name=_('Dígito'), null=True, blank=True)
    pix_1 = models.CharField(max_length=250, verbose_name=_('Chave PIX'), null=True, blank=True)
    pix_2 = models.CharField(max_length=250, verbose_name=_('Chave PIX'), null=True, blank=True)
    obs_bank = models.TextField(max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # Historico
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        if self.cpf:
            cpf = str(self.cpf).zfill(11).replace('.', '').replace('-', '')
            return f'{self.name} {self.last_name} - {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
        elif self.cnpj:
            cnpj = str(self.cnpj).zfill(14).replace('.', '').replace('/', '').replace('-', '')
            return f'{self.nome_fantasia} - {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
        else:
            return _('Cadastro sem Identificação')
