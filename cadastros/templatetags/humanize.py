from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()

@register.filter
def cnpj_format(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'

@register.filter
def cpf_format(cpf):
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
