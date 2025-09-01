from django.urls import path
from .views import CadastroPessoa, EditarPessoa, BuscaPessoa, PessoaDeleteView
from .views import CadastroEmpresa, EditarEmpresa, BuscaEmpresa, EmpresaDeleteView, Agenda
from .views import CadastroHistoricoView
from .views import CadastroPessoaDetail, CadastroEmpresaDetail


urlpatterns = [
    # Pessoa
    path('pf/', BuscaPessoa.as_view(), name='pessoa-busca'),
    path('pf/add/', CadastroPessoa.as_view(), name='pessoa-cadastro'),
    path('pf/<int:pk>/', CadastroPessoaDetail.as_view(), name='pessoa-detail'),
    path('pf/<int:pk>/edit/', EditarPessoa.as_view(), name='pessoa-edit'),
    path('pf/<int:pk>/del/', PessoaDeleteView.as_view(), name='pessoa-delete'),
    # Empresa
    path('pj/', BuscaEmpresa.as_view(), name='empresa-busca'),
    path('pj/add/', CadastroEmpresa.as_view(), name='empresa-cadastro'),
    path('pj/<int:pk>/', CadastroEmpresaDetail.as_view(), name='empresa-detail'),
    path('pj/<int:pk>/edit/', EditarEmpresa.as_view(), name='empresa-edit'),
    path('pj/<int:pk>/del/', EmpresaDeleteView.as_view(), name='empresa-delete'),
    # Utilitarios
    path('agenda/', Agenda.as_view(), name='agenda-telefonica'),
    path('cadastro/<int:pk>/log/', CadastroHistoricoView.as_view(), name='log-cadastro'),
]
