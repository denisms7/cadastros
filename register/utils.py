from itertools import cycle
from django.core.cache import cache
import requests
import logging


CACHE_KEY = 'bank_list'
CACHE_TIMEOUT = 60 * 60  # 1 hora
logger = logging.getLogger(__name__)


def cpf_validate(cpf: str) -> bool:
    TAMANHO_CPF = 11
    cpf = cpf.replace('.', '').replace('-', '').replace('/', '')
    if len(cpf) != TAMANHO_CPF:
        return False
    if not cpf.isdigit():
        return False
    if cpf in (c * TAMANHO_CPF for c in "1234567890"):
        return False
    cpf_reverso = cpf[::-1]
    for i in range(2, 0, -1):
        cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
        dv_calculado = sum(map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
        if cpf_reverso[i - 1:i] != str(dv_calculado % 10):
            return False
    return True


def cnpj_validate(cnpj: str) -> bool:
    LENGTH_CNPJ = 14
    cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
    if len(cnpj) != LENGTH_CNPJ:
        return False
    if not cnpj.isdigit():
        return False
    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return False
    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False
    return True


def get_bank():
    # Tenta pegar do cache
    bancos = cache.get(CACHE_KEY)
    if bancos is not None:
        return bancos

    # Se não estiver no cache, busca da API
    url = 'https://brasilapi.com.br/api/banks/v1'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        logger.error(f'Erro ao buscar bancos: {e}')
        return [(0, '---------')]

    bancos = [(bank['code'], f"{bank['code']} - {bank['name']}") for bank in data if bank.get('code')]
    bancos.sort()
    bancos = [(0, '---------')] + bancos

    # Salva no cache
    cache.set(CACHE_KEY, bancos, CACHE_TIMEOUT)
    return bancos
