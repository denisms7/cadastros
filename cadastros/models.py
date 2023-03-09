from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Cadastro_Empresa(models.Model):
    STATUS_CHOICES = [
        (1, _('Ativo')),
        (0, _('Inativo')),
    ]

    CONTATOS_CHOICES = [
        (1, _('Telefone')),
        (2, _('WhatsApp')),
    ]

    # Sistema
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, verbose_name=_('Status do Cadastro'))
    cadastrado_em = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Data de Cadastro'))
    cadastrado_por = models.ForeignKey(
        User, default=1, on_delete=models.PROTECT, verbose_name=_('Cadastrado por'), null=True, blank=True)
    # Dados Pessoais
    pessoa_juridica = models.CharField(max_length=200, verbose_name=_('Razão Social'))
    nome_fantasia = models.CharField(max_length=200, verbose_name=_('Nome Fantasia'))
    cnpj = models.CharField(max_length=14, unique=True, verbose_name=_('CNPJ'))
    is_estadual = models.CharField(max_length=14, verbose_name=_('Incrição Estadual'), null=True, blank=True)
    is_municipal = models.CharField(max_length=14, verbose_name=_('Incrição Municipal'), null=True, blank=True)
    # E-mail
    email_1 = models.EmailField(max_length=150, verbose_name=_(
        'E-mail 01'), null=True, blank=True)
    email_2 = models.EmailField(max_length=150, verbose_name=_(
        'E-mail 02'), null=True, blank=True)
    # Contato 01
    fone_1 = models.CharField(max_length=15, verbose_name=_('Contato 01'), null=True, blank=True)
    fone_1_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 01 Tipo'), default=1, choices=CONTATOS_CHOICES, null=True, blank=True)
    # Contato 02
    fone_2 = models.CharField(max_length=15, verbose_name=_('Contato 02'), null=True, blank=True)
    fone_2_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 02 Tipo'), default=1, choices=CONTATOS_CHOICES, null=True, blank=True)
    # Contato 03
    fone_3 = models.CharField(max_length=15, verbose_name=_('Contato 03'), null=True, blank=True)
    fone_3_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 03 Tipo'), default=1, choices=CONTATOS_CHOICES, null=True, blank=True)
    # Link
    link_1 = models.URLField(verbose_name=_('Link 01'), null=True, blank=True)
    link_2 = models.URLField(verbose_name=_('Link 02'), null=True, blank=True)
    obs_contato = models.TextField(max_length=2000, verbose_name=_(
        'Observações'), null=True, blank=True)
    # Endereço
    cep = models.CharField(
        max_length=8, verbose_name='CEP', null=True, blank=True)
    estado = models.CharField(max_length=2, verbose_name=_(
        'Estado'), null=True, blank=True)
    cidade = models.CharField(max_length=200, verbose_name=_(
        'Cidade'), null=True, blank=True)
    bairro = models.CharField(max_length=200, verbose_name=_(
        'Bairro'), null=True, blank=True)
    endereco = models.CharField(max_length=250, verbose_name=_(
        'Endereço'), null=True, blank=True)
    numero = models.IntegerField(
        default=0, verbose_name=_('Número'), null=True, blank=True)
    complemento = models.CharField(max_length=250, verbose_name=_(
        'Complemento'), null=True, blank=True)
    obs_endereco = models.TextField(
        max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    ultima_att = models.CharField(max_length=200, verbose_name=_('Última Atualização'), null=True, blank=True)
    data_att = models.DateTimeField(verbose_name=_('Data de Atualização'), null=True, blank=True)

    def __str__(self):
        return f"{self.nome_fantasia} - {self.cnpj[0:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:14]}"

# PESSOA


class Cadastro_Pessoa(models.Model):
    SEXO_CHOICES = [
        ('M', _('Masculino')),
        ('F', _('Feminino')),
        ('O', _('Outros')),
    ]

    STATUS_CHOICES = [
        (1, _('Ativo')),
        (0, _('Inativo')),
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

    # Sistema
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, verbose_name=_('Status do Cadastro'))
    cadastrado_em = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Data de Cadastro'))
    cadastrado_por = models.ForeignKey(
        User, default=1, on_delete=models.PROTECT, verbose_name=_('Cadastrado por'), null=True, blank=True)
    # Dados Pessoais
    primeiro_nome = models.CharField(max_length=50, verbose_name=_('Nome'))
    ultimo_nome = models.CharField(max_length=150, verbose_name=_('Sobrenome'))
    cpf = models.CharField(max_length=11, unique=True, verbose_name=_('CPF'))
    rg = models.CharField(max_length=11, verbose_name=_(
        'RG'), null=True, blank=True)
    rg_emissor = models.CharField(
        max_length=3, verbose_name=_('Emissor'), null=True, blank=True)
    rg_expedicao = models.DateField(
        verbose_name=_('Expedicao'), null=True, blank=True)
    nascimento = models.DateField(verbose_name=_(
        'Nascimento'), null=True, blank=True)
    escolaridade = models.PositiveSmallIntegerField(choices=ESCOLARIDADE_CHOICES, verbose_name=_(
        'Escolaridade'), null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name=_(
        'Sexo'), null=True, blank=True)
    estado_civil = models.PositiveSmallIntegerField(choices=ESTADO_CIVIL_CHOICES, verbose_name=_(
        'Estado Civil'), null=True, blank=True)
    # Conjuge
    conjuge_primeiro_nome = models.CharField(
        max_length=50, verbose_name=_('Nome do Conjuge'), null=True, blank=True)
    conjuge_ultimo_nome = models.CharField(max_length=150, verbose_name=_(
        'Sobrenome do Conjuge'), null=True, blank=True)
    # Mãe
    mae_primeiro_nome = models.CharField(
        max_length=50, verbose_name=_('Nome da Mãe'), null=True, blank=True)
    mae_ultimo_nome = models.CharField(max_length=150, verbose_name=_(
        'Sobrenome da Mãe'), null=True, blank=True)
    # Pai
    pai_primeiro_nome = models.CharField(
        max_length=50, verbose_name=_('Nome do Pai'), null=True, blank=True)
    pai_ultimo_nome = models.CharField(max_length=150, verbose_name=_(
        'Sobrenome do Pai'), null=True, blank=True)
    obs_pessoal = models.TextField(max_length=2000, verbose_name=_(
        'Observações'), null=True, blank=True)
    # E-mail
    email_1 = models.EmailField(max_length=150, verbose_name=_(
        'E-mail 01'), null=True, blank=True)
    email_2 = models.EmailField(max_length=150, verbose_name=_(
        'E-mail 02'), null=True, blank=True)
    # Contato 01
    fone_1 = models.CharField(max_length=15, verbose_name=_('Contato 01'), null=True, blank=True)
    fone_1_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 01 Tipo'), default=1, choices=CONTATOS_CHOICES, null=True, blank=True)
    # Contato 02
    fone_2 = models.CharField(max_length=15, verbose_name=_('Contato 02'), null=True, blank=True)
    fone_2_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 02 Tipo'), default=1, choices=CONTATOS_CHOICES, null=True, blank=True)
    # Contato 03
    fone_3 = models.CharField(max_length=15, verbose_name=_('Contato 03'), null=True, blank=True)
    fone_3_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 03 Tipo'), default=1, choices=CONTATOS_CHOICES, null=True, blank=True)
    # Link
    link_1 = models.URLField(verbose_name=_('Link 01'), null=True, blank=True)
    link_2 = models.URLField(verbose_name=_('Link 02'), null=True, blank=True)
    obs_contato = models.TextField(max_length=2000, verbose_name=_(
        'Observações'), null=True, blank=True)
    # Endereço
    cep = models.CharField(
        max_length=8, verbose_name='CEP', null=True, blank=True)
    estado = models.CharField(max_length=2, verbose_name=_(
        'Estado'), null=True, blank=True)
    cidade = models.CharField(max_length=200, verbose_name=_(
        'Cidade'), null=True, blank=True)
    bairro = models.CharField(max_length=200, verbose_name=_(
        'Bairro'), null=True, blank=True)
    endereco = models.CharField(max_length=250, verbose_name=_(
        'Endereço'), null=True, blank=True)
    numero = models.IntegerField(
        default=0, verbose_name=_('Número'), null=True, blank=True)
    complemento = models.CharField(max_length=250, verbose_name=_(
        'Complemento'), null=True, blank=True)
    obs_endereco = models.TextField(
        max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    ultima_att = models.CharField(max_length=200, verbose_name=_('Última Atualização'), null=True, blank=True)
    data_att = models.DateTimeField(verbose_name=_('Data de Atualização'), null=True, blank=True)

    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome} - {self.cpf[0:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:11]}'
    