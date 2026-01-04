# 📟 Cadastro Django
Sistema completo de Cadastro de Pessoas Físicas e Jurídicas com Django, incluindo log de auditoria detalhado, validações automáticas, sistema de permissões e interface responsiva com Bootstrap

<div align="center">
  <img width="50%" src="https://user-images.githubusercontent.com/82631808/218283234-3c42a1f5-40e6-4175-88df-aacaf0e0a81e.png" alt="Pessoa"/>
  <img width="50%" src="https://user-images.githubusercontent.com/82631808/218283236-a1b0e8f4-6e10-4eff-88ff-d7b2a23b119f.png" alt="Empresa"/>
</div>

### 🚀 Tecnologias
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![jQuery](https://img.shields.io/badge/jquery-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

<hr>

## ✨ Funcionalidades

### Cadastro de Pessoas Físicas
* Dados pessoais completos (nome, CPF, RG, data de nascimento)
* Opções inclusivas de gênero (cisgênero, transgênero, não-binário)
* Informações de CNH (número, categoria, validade)
* Dados familiares (cônjuge, pais)
* Níveis detalhados de escolaridade

### Cadastro de Pessoas Jurídicas
* Razão social e nome fantasia
* CNPJ com validação automática
* Informações empresariais (porte, atividade, situação)
* Inscrições estadual e municipal

### Recursos Gerais
* **Sistema de auditoria**: Histórico completo de alterações com django-simple-history
* **Logs individualizados**: Visualização de histórico separado por PF e PJ
* **Dados bancários**: Conta, agência, PIX (até 2 chaves)
* **Sistema de contatos**: Múltiplos telefones, e-mails e links
* **Endereço completo**: CEP, estado, cidade, bairro, complemento
* **Sistema de permissões**: Controle de acesso baseado em permissões do Django
* **Busca avançada**: Filtros por nome, CPF/CNPJ
* **Paginação**: Listagem organizada com 10 itens por página
* **Validações JavaScript**: Máscaras automáticas para CPF, CNPJ, telefone, CEP
* **Agenda de contatos**: Visualização consolidada de todos os cadastros

## 🏗️ Arquitetura

O sistema utiliza **Proxy Models** para separar Pessoas Físicas e Jurídicas:
* Modelo base único (`Register`) com campo `type` (0=PF, 1=PJ)
* `PessoaFisica` e `PessoaJuridica` como proxy models
* Managers customizados para filtrar automaticamente por tipo
* Admin do Django configurado separadamente para cada tipo

## 📟 Executar este modelo
### 📋 Pré-requisitos
* Python 3.11 ou superior
* Bootstrap 5.3.0
* pip atualizado

### 🛠️ Configuração e Implantação
Crie um ambiente virtual:
```
python -m venv env
```

Ative o ambiente virtual e instale as dependências:

**Windows:**
```
env\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac:**
```
source env/bin/activate
pip install -r requirements.txt
```

**OBS:** Caso ocorra algum erro, atualize o pip:
```
python -m pip install --upgrade pip
```

**Dependências principais:**
* `Django==5.2.5` - Framework web
* `django-simple-history==3.10.1` - Sistema de auditoria
* `django-widget-tweaks==1.5.0` - Customização de formulários
* `django-humanize==0.1.2` - Formatação de dados
* `django-braces==1.15.0` - Mixins úteis para views

Execute o comando de migração no terminal do ambiente virtural para criação das tabelas e do banco de dados.
```
python manage.py migrate
```

Crie um super usuario executando o compando e informe os dados solicitados.
```
python manage.py createsuperuser
```

Execute o comando abaixo:
```
python manage.py runserver
```
Este comando ira executar o sistema e estará acessivel via IP http://127.0.0.1:8000/ para os testes das funcionalidades.

O sistema necessita de um usuario logado, para salvar o registro no banco de dados, para afetuar login acesse http://127.0.0.1:8000/admin/ e efetue login com o usuario criado anteriormente.

### 🔗 URLs disponíveis
* **Admin**: http://127.0.0.1:8000/admin/
* **Pessoas Físicas**: http://127.0.0.1:8000/pf/
* **Pessoas Jurídicas**: http://127.0.0.1:8000/pj/
* **Agenda de Contatos**: http://127.0.0.1:8000/agenda/

## 📦 Implantação do módulo `register` em outros sistemas

O módulo `register` pode ser reutilizado em outros projetos Django.

### 📋 Pré-requisitos
* Python 3.11 ou superior
* Django 5.2 ou superior
* Bootstrap 5.3

### 🛠️ Configuração

**1. Instale as dependências:**
```bash
pip install -r requirements.txt
```

Bibliotecas principais necessárias:
* `Django==5.2.5`
* `django-simple-history==3.10.1` - Auditoria e histórico
* `django-widget-tweaks==1.5.0` - Customização de widgets de formulário
* `django-humanize==0.1.2` - Formatação de datas e números

**2. Configure o `settings.py`:**

Adicione os apps em `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',           # Customização de formulários
    'django.contrib.humanize',  # Formatação humanizada
    'simple_history',           # Auditoria e histórico
    'register',                 # Módulo de cadastros
]
```

Adicione o middleware do simple_history:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',  # Middleware de auditoria
]
```

Configure os arquivos estáticos:
```python
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```

Configure os templates:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'app' / 'templates',
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**3. Configure as URLs no arquivo `urls.py` principal:**
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),  # URLs do módulo register
]
```

**4. Execute as migrações:**
```bash
python manage.py migrate
```

**5. Crie um superusuário:**
```bash
python manage.py createsuperuser
```

**6. Templates base necessários:**

O sistema requer templates base na pasta `templates/` na raiz do projeto:
* `theme.html` - Template base com Bootstrap 5.3
* `pagination.html` - Componente de paginação
* `alerts.html` - Sistema de mensagens/alertas

**7. Arquivos JavaScript incluídos:**

O módulo inclui validações e máscaras JavaScript em `register/static/cadastros/`:
* `jQuery-v3.6.4.js` - jQuery
* `jQuery Mask Plugin v1.14.16.js` - Máscaras de input
* `validacao.js` - Validação de CPF/CNPJ
* `verifica_campos.js` - Validação de campos
* `cadastro.js` - Funções principais do cadastro

### 🔐 Permissões

O sistema utiliza o sistema de permissões do Django. As permissões disponíveis:
* `register.view_pessoafisica` - Visualizar pessoas físicas
* `register.add_pessoafisica` - Adicionar pessoas físicas
* `register.change_pessoafisica` - Editar pessoas físicas
* `register.delete_pessoafisica` - Deletar pessoas físicas
* `register.view_pessoajuridica` - Visualizar pessoas jurídicas
* `register.add_pessoajuridica` - Adicionar pessoas jurídicas
* `register.change_pessoajuridica` - Editar pessoas jurídicas
* `register.delete_pessoajuridica` - Deletar pessoas jurídicas

Configure as permissões para grupos/usuários através do Django Admin.

## 📂 Estrutura de URLs

O módulo `register` fornece as seguintes rotas:

### Pessoas Físicas (PF)
* `/pf/` - Listagem de pessoas físicas
* `/pf/0/adicionar/` - Adicionar nova pessoa física
* `/pf/<id>/visualizar/` - Visualizar detalhes
* `/pf/<id>/editar/` - Editar cadastro
* `/pf/<id>/deletar/` - Deletar cadastro
* `/pf/<id>/log/` - Histórico de alterações

### Pessoas Jurídicas (PJ)
* `/pj/` - Listagem de pessoas jurídicas
* `/pj/0/adicionar/` - Adicionar nova pessoa jurídica
* `/pj/<id>/visualizar/` - Visualizar detalhes
* `/pj/<id>/editar/` - Editar cadastro
* `/pj/<id>/deletar/` - Deletar cadastro
* `/pj/<id>/log/` - Histórico de alterações

### Utilitários
* `/agenda/` - Agenda consolidada de contatos

## 🗄️ Modelos de Dados

### Register (Modelo Base)
Modelo principal que armazena tanto pessoas físicas quanto jurídicas. Campos principais:
* `type` - Tipo de cadastro (0=PF, 1=PJ)
* `active` - Status ativo/inativo
* `created_at` - Data de criação
* `created_by` - Usuário que criou

### PessoaFisica (Proxy Model)
Proxy model que filtra apenas registros com `type=0`. Campos específicos:
* `name`, `last_name` - Nome completo
* `cpf`, `rg` - Documentos
* `birth` - Data de nascimento
* `sex` - Gênero/sexo
* `education` - Escolaridade
* `spouse_status`, `spouse_name` - Dados do cônjuge
* `mother_name`, `father_name` - Filiação
* `cnh_n`, `cnh_category` - CNH

### PessoaJuridica (Proxy Model)
Proxy model que filtra apenas registros com `type=1`. Campos específicos:
* `legal` - Razão social
* `fantasy` - Nome fantasia
* `cnpj` - CNPJ
* `cnpj_situation` - Situação cadastral
* `cnpj_carrying` - Porte da empresa
* `cnpj_date` - Data de abertura
* `cnpj_activity` - Atividade principal
* `n_state`, `n_municipal` - Inscrições

### Campos Compartilhados (PF e PJ)
* **Contatos**: `email_1`, `email_2`, `phone_1`, `phone_2`, `phone_3`, `link_1`, `link_2`
* **Endereço**: `cep`, `state`, `city`, `neighborhood`, `address`, `number`, `complement`
* **Dados Bancários**: `bank`, `agency`, `account`, `digit`, `pix_1`, `pix_2`, `title_holder`, `document_holder`
* **Observações**: `obs`, `obs_contact`, `obs_address`, `obs_bank`

## ✒️ Autor
* **Desenvolvedor** - *Denis Muniz Silva* 

### 📞 Contatos
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?phone=5543991038557) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/denisms/) [![Email](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:denis.m.s.777@hotmail.com?) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/de.muniz/) 
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/denisms3/) 


