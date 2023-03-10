# Generated by Django 4.1.6 on 2023-03-09 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Ativo'), (0, 'Inativo')], verbose_name='Status do Cadastro')),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('primeiro_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('ultimo_nome', models.CharField(max_length=150, verbose_name='Sobrenome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('rg_emissor', models.CharField(blank=True, max_length=3, null=True, verbose_name='Emissor')),
                ('rg_expedicao', models.DateField(blank=True, null=True, verbose_name='Expedicao')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Nascimento')),
                ('escolaridade', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Sem Ensino'), (2, 'Fundamental - Incompleto'), (3, 'Fundamental - Completo'), (4, 'Médio - Incompleto'), (5, 'Médio - Completo'), (6, 'Superior - Incompleto'), (7, 'Superior - Completo'), (8, 'Pós-graduação (Lato senso) - Incompleto'), (9, 'Pós-graduação (Lato senso) - Completo'), (10, 'Pós-graduação (Stricto sensu, nível mestrado) - Incompleto'), (11, 'Pós-graduação (Stricto sensu, nível mestrado) - Completo'), (12, 'Pós-graduação (Stricto sensu, nível doutor) - Incompleto'), (13, 'Pós-graduação (Stricto sensu, nível doutor) - Completo')], null=True, verbose_name='Escolaridade')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, null=True, verbose_name='Sexo')),
                ('estado_civil', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Casado'), (2, 'Divorciado'), (3, 'Solteiro'), (4, 'União Estavel'), (5, 'Viúvo')], null=True, verbose_name='Estado Civil')),
                ('conjuge_primeiro_nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do Conjuge')),
                ('conjuge_ultimo_nome', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sobrenome do Conjuge')),
                ('mae_primeiro_nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome da Mãe')),
                ('mae_ultimo_nome', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sobrenome da Mãe')),
                ('pai_primeiro_nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do Pai')),
                ('pai_ultimo_nome', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sobrenome do Pai')),
                ('obs_pessoal', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('email_1', models.EmailField(blank=True, max_length=150, null=True, verbose_name='E-mail 01')),
                ('email_2', models.EmailField(blank=True, max_length=150, null=True, verbose_name='E-mail 02')),
                ('fone_1', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 01')),
                ('fone_1_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Telefone'), (2, 'WhatsApp')], default=1, null=True, verbose_name='Contato 01 Tipo')),
                ('fone_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 02')),
                ('fone_2_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Telefone'), (2, 'WhatsApp')], default=1, null=True, verbose_name='Contato 02 Tipo')),
                ('fone_3', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 03')),
                ('fone_3_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Telefone'), (2, 'WhatsApp')], default=1, null=True, verbose_name='Contato 03 Tipo')),
                ('link_1', models.URLField(blank=True, null=True, verbose_name='Link 01')),
                ('link_2', models.URLField(blank=True, null=True, verbose_name='Link 02')),
                ('obs_contato', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cidade')),
                ('bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco', models.CharField(blank=True, max_length=250, null=True, verbose_name='Endereço')),
                ('numero', models.IntegerField(blank=True, default=0, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=250, null=True, verbose_name='Complemento')),
                ('obs_endereco', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('ultima_att', models.CharField(blank=True, max_length=200, null=True, verbose_name='Última Atualização')),
                ('data_att', models.DateTimeField(blank=True, null=True, verbose_name='Data de Atualização')),
                ('cadastrado_por', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Cadastrado por')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Ativo'), (0, 'Inativo')], verbose_name='Status do Cadastro')),
                ('cadastrado_em', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('pessoa_juridica', models.CharField(max_length=200, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(max_length=200, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=14, unique=True, verbose_name='CNPJ')),
                ('is_estadual', models.CharField(blank=True, max_length=14, null=True, verbose_name='Incrição Estadual')),
                ('is_municipal', models.CharField(blank=True, max_length=14, null=True, verbose_name='Incrição Municipal')),
                ('email_1', models.EmailField(blank=True, max_length=150, null=True, verbose_name='E-mail 01')),
                ('email_2', models.EmailField(blank=True, max_length=150, null=True, verbose_name='E-mail 02')),
                ('fone_1', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 01')),
                ('fone_1_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Telefone'), (2, 'WhatsApp')], default=1, null=True, verbose_name='Contato 01 Tipo')),
                ('fone_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 02')),
                ('fone_2_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Telefone'), (2, 'WhatsApp')], default=1, null=True, verbose_name='Contato 02 Tipo')),
                ('fone_3', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 03')),
                ('fone_3_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Telefone'), (2, 'WhatsApp')], default=1, null=True, verbose_name='Contato 03 Tipo')),
                ('link_1', models.URLField(blank=True, null=True, verbose_name='Link 01')),
                ('link_2', models.URLField(blank=True, null=True, verbose_name='Link 02')),
                ('obs_contato', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cidade')),
                ('bairro', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bairro')),
                ('endereco', models.CharField(blank=True, max_length=250, null=True, verbose_name='Endereço')),
                ('numero', models.IntegerField(blank=True, default=0, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=250, null=True, verbose_name='Complemento')),
                ('obs_endereco', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observações')),
                ('ultima_att', models.CharField(blank=True, max_length=200, null=True, verbose_name='Última Atualização')),
                ('data_att', models.DateTimeField(blank=True, null=True, verbose_name='Data de Atualização')),
                ('cadastrado_por', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Cadastrado por')),
            ],
        ),
    ]
