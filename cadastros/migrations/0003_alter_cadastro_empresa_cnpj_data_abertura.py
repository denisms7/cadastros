# Generated by Django 4.1.6 on 2023-03-11 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_cadastro_empresa_cnpj_atividade_principal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_empresa',
            name='cnpj_data_abertura',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Abertura'),
        ),
    ]