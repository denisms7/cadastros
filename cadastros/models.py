from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

class Cadastro(models.Model):
    SEXO_CHOICES = [
        ('M', _('Masculino')),
        ('F', _('Feminino')),
        ('O', _('Outros')),
        ('-', _('Não Informado')),
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

    CONTA_TIPO_CHOICES = [
        (1, _('Conta Corrente')),
        (2, _('Conta Salário')),
        (3, _('Conta Poupança')),
    ]

    TIPO_DOCUMENTO_CHOICES = [
        (0, _('CPF')),
        (1, _('CNPJ')),
    ]

    CHOICES_CATEGORIA_CNH = [
        (1, _('A')),
        (2, _('B')),
        (3, _('AB')),
        (4, _('C')),
        (5, _('D')),
        (6, _('E')),
    ]

    TIPO_CHOICES = [
        (0, _('Pessoa Física')),
        (1, _('Pessoa Jurídica')),
    ]

    # Sistema
    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES, verbose_name=_('Tipo'), default=0)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, verbose_name=_('Status do Cadastro'), default=1)
    cadastrado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de Cadastro'))
    cadastrado_por = models.ForeignKey(User, default=1, on_delete=models.PROTECT, verbose_name=_('Cadastrado por'))
    
    # Dados da Empresa
    pessoa_juridica = models.CharField(max_length=200, verbose_name=_('Razão Social'), null=True, blank=True)
    nome_fantasia = models.CharField(max_length=200, verbose_name=_('Nome Fantasia'), null=True, blank=True)
    is_estadual = models.CharField(max_length=14, verbose_name=_('Incrição Estadual'), null=True, blank=True)
    is_municipal = models.CharField(max_length=14, verbose_name=_('Incrição Municipal'), null=True, blank=True)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name=_('CNPJ'), null=True, blank=True)
    cnpj_situacao = models.CharField(max_length=200, verbose_name=_('Situação'), null=True, blank=True)
    cnpj_porte = models.CharField(max_length=200, verbose_name=_('Porte de Empresa'), null=True, blank=True)
    cnpj_data_abertura = models.DateField(verbose_name=_('Data de Abertura'), null=True, blank=True) 
    cnpj_tipo = models.CharField(max_length=200, verbose_name=_('Tipo'), null=True, blank=True)
    cnpj_atividade_principal = models.TextField(max_length=2000, verbose_name=_('Atividade Principal'), null=True, blank=True)
    
    # Dados Pessoais
    primeiro_nome = models.CharField(max_length=50, verbose_name=_('Nome'), null=True, blank=True)
    ultimo_nome = models.CharField(max_length=150, verbose_name=_('Sobrenome'), null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name=_('CPF'), null=True, blank=True)
    rg = models.CharField(max_length=11, verbose_name=_('RG (legado)'), null=True, blank=True)
    rg_emissor = models.CharField(max_length=3, verbose_name=_('Emissor'), null=True, blank=True)
    rg_expedicao = models.DateField(verbose_name=_('Expedicao'), null=True, blank=True)
    nascimento = models.DateField(verbose_name=_('Nascimento'), null=True, blank=True)
    escolaridade = models.PositiveSmallIntegerField(choices=ESCOLARIDADE_CHOICES, verbose_name=_('Escolaridade'), null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name=_('Sexo'), null=True, blank=True)
    estado_civil = models.PositiveSmallIntegerField(choices=ESTADO_CIVIL_CHOICES, verbose_name=_('Estado Civil'), null=True, blank=True)
    # = Conjuge
    conjuge_primeiro_nome = models.CharField(max_length=50, verbose_name=_('Nome do Conjuge'), null=True, blank=True)
    conjuge_ultimo_nome = models.CharField(max_length=150, verbose_name=_('Sobrenome do Conjuge'), null=True, blank=True)
    # = Pais
    mae_primeiro_nome = models.CharField(max_length=50, verbose_name=_('Nome da Mãe'), null=True, blank=True)
    mae_ultimo_nome = models.CharField(max_length=150, verbose_name=_('Sobrenome da Mãe'), null=True, blank=True)
    pai_primeiro_nome = models.CharField(max_length=50, verbose_name=_('Nome do Pai'), null=True, blank=True)
    pai_ultimo_nome = models.CharField(max_length=150, verbose_name=_('Sobrenome do Pai'), null=True, blank=True)
    obs_pessoal = models.TextField(max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # = CNH
    cnh_n = models.CharField(max_length=50, verbose_name=_('CNH'), null=True, blank=True)
    cnh_emissao = models.DateField(verbose_name=_('Emissão'), null=True, blank=True)
    cnh_validade = models.DateField(verbose_name=_('Validade'), null=True, blank=True)
    cnh_categoria = models.PositiveSmallIntegerField(choices=CHOICES_CATEGORIA_CNH, verbose_name=_('Categoria'), null=True, blank=True)
    
    # =======================================================================================
    # E-mail
    email_1 = models.EmailField(max_length=150, verbose_name=_('E-mail'), null=True, blank=True)
    email_2 = models.EmailField(max_length=150, verbose_name=_('E-mail'), null=True, blank=True)
    # Contato 01
    fone_1 = models.CharField(max_length=15, verbose_name=_('Contato'), null=True, blank=True)
    fone_1_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 01 Tipo'), choices=CONTATOS_CHOICES, null=True, blank=True)
    # Contato 02
    fone_2 = models.CharField(max_length=15, verbose_name=_('Contato'), null=True, blank=True)
    fone_2_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 02 Tipo'), choices=CONTATOS_CHOICES, null=True, blank=True)
    # Contato 03
    fone_3 = models.CharField(max_length=15, verbose_name=_('Contato'), null=True, blank=True)
    fone_3_tipo = models.PositiveSmallIntegerField(verbose_name=_('Contato 03 Tipo'), choices=CONTATOS_CHOICES, null=True, blank=True)
    # Link
    link_1 = models.URLField(verbose_name=_('Link'), null=True, blank=True)
    link_2 = models.URLField(verbose_name=_('Link'), null=True, blank=True)
    obs_contato = models.TextField(max_length=2000, verbose_name=_('Observações'), null=True, blank=True)
    # Endereço
    cep = models.CharField(
        max_length=10, verbose_name='CEP', null=True, blank=True)
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

    # Banco
    nome_razao_titular = models.CharField(max_length=50, verbose_name=_('Nome/Razão'), null=True, blank=True)
    tipo_de_documento = models.PositiveSmallIntegerField(choices=TIPO_DOCUMENTO_CHOICES, verbose_name=_('Tipo de Documento'), null=True, blank=True)
    documento_titular = models.CharField(max_length=18, verbose_name=_('CPF/CNPJ'), null=True, blank=True)
    tipo_de_conta = models.PositiveSmallIntegerField(choices=CONTA_TIPO_CHOICES, verbose_name=_('Tipo de Conta'), null=True, blank=True)
    n_banco = models.IntegerField(default=0, verbose_name=_('N° Banco'), null=True, blank=True)
    agencia = models.CharField(max_length=10, verbose_name=_('Agencia'), null=True, blank=True)
    conta = models.CharField(max_length=50, verbose_name=_('N° Conta'), null=True, blank=True)
    digito = models.CharField(max_length=5, verbose_name=_('Dígito'), null=True, blank=True)
    pix_1 = models.CharField(max_length=250, verbose_name=_('Chave PIX'), null=True, blank=True)
    pix_2 = models.CharField(max_length=250, verbose_name=_('Chave PIX'), null=True, blank=True)
    obs_banco = models.TextField(
        max_length=2000, verbose_name=_('Observações'), null=True, blank=True)

    history = HistoricalRecords(inherit=True)

    def __str__(self):
        if self.cpf:
            cpf = str(self.cpf).zfill(11).replace('.', '').replace('-', '')
            return f'{self.primeiro_nome} {self.ultimo_nome} - {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
        elif self.cnpj:
            cnpj = str(self.cnpj).zfill(14).replace('.', '').replace('/', '').replace('-', '')
            return f'{self.nome_fantasia} - {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
        else:
            return 'Cadastro sem Identificação'
        
