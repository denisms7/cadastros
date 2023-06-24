# 📟 Cadastro Django
App modelo de Cadastro de Pessoa em Django para uso em sistemas diversos

<div align="center">
  <img height="180em" src="https://user-images.githubusercontent.com/82631808/218283233-685611a5-7d42-4ef9-be5d-92e7cc11f1bf.png"/>
  <img height="180em" src="https://user-images.githubusercontent.com/82631808/218283234-3c42a1f5-40e6-4175-88df-aacaf0e0a81e.png"/>
</div>
<div align="center">
  <img height="180em" src="https://user-images.githubusercontent.com/82631808/218283236-a1b0e8f4-6e10-4eff-88ff-d7b2a23b119f.png"/>
  <img height="180em" src="https://user-images.githubusercontent.com/82631808/218283237-b6bbefe5-31e8-4f33-aa32-f61e9f0ff48c.png"/>
</div>

### 🚀 Tecnologias
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

<hr>

## 📟 Executar este modelo
### 📋 Pré-requisitos
* Python 3.11
* Bootstrap 5.3.0

### 🛠️ Configuração e Implantação
Crie um ambiente virtual:
```
python -m venv env
```

Ative o ambiente virtual e apos isso instale as bibliotecas do arquivo [requirements.txt](https://github.com/denisms7/cadastro-djhango/blob/main/requirements.txt)
```
pip install -r requirements.txt
```

OBS: Caso ocorra algum erro efetue a atualização do pip
```
python -m pip install --upgrade pip
```

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

O sistema necessita de um usuario logado, para salvar o registro no banco de dados, para afetuar login acesse http://127.0.0.1:8000/admin/ e efetue login com o usuario criado anteriormente, para acessar o sistema apos logado basta acessar a URL http://127.0.0.1:8000/ como anteriormente citado.

## 📦 Implantação destes modulos em outros sistemas
* cadastro_empresa
* cadastro_pessoa

### 📋 Pré-requisitos
* Bootstrap 5.3
* Python 3.8.2

### 🛠️ Configuração
Crie um ambiente virtual utilizando as bibliotecas do arquivo [requirements.txt](https://github.com/denisms7/cadastro-djhango/blob/main/requirements.txt)

Execute o comando de migração no terminal do ambiente virtural para criação das tabelas e do banco de dados:
```
python manage.py migrate
```

Crie um super usuario executando o compando:
```
python manage.py createsuperuser
```

O sistema necessita de um usuario logado ou um usuario com ID/PK 1, para salvar o registro no banco de dados

Configurar variavel INSTALLED_APPS acrescentando com os APPS e Libs baixo:
```
INSTALLED_APPS = [
    ...
    'widget_tweaks',
    'django.contrib.humanize',
    'cadastro_pessoa.apps.CadastroPessoaConfig', 
    'cadastro_empresa.apps.CadastroEmpresaConfig', 
    ...
    
]
```

Configurar as variaveis STATIC_URL e STATICFILES_DIRS conforme abaixo:
```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

Configurar a variável TEMPLATES conforme abaixo:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

Configurar a variavel urlpatterns no arquivo urls.py com as URLS desejadas:
```
urlpatterns = [
    ...
    path('', include('cadastro_pessoa.urls')),
    path('', include('cadastro_empresa.urls')),
    ...
]
```

Os templates dos modulos cadastro_empresa e cadastro_pessoa necessitam de um template base com e um template de paginação como os disponiveis no modulo nav_bar > templates 



## ✒️ Autor
* **Desenvolvedor** - *Denis Muniz Silva* 

### 📞 Contatos
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://api.whatsapp.com/send?phone=5543991038557) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/denisms/) [![Email](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:denis.m.s.777@hotmail.com?) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/de.muniz/) 
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/denisms3/) 


