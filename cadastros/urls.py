from django.urls import path
from .views import CadastroPessoa, EditarPessoa, BuscaPessoa, DeletePessoa
from .views import CadastroEmpresa, EditarEmpresa, BuscaEmpresa, DeleteEmpresa, Agenda

urlpatterns = [
    path('pf-add/', CadastroPessoa.as_view(), name='pessoa-cadastro'),
    path('pf-edit/<int:pk>', EditarPessoa.as_view(), name='pessoa-edit'),
    path('pf-loc/', BuscaPessoa.as_view(), name='pessoa-busca'),
    path('pf-del/<int:pk>', DeletePessoa, name='pessoa-delete'),
    
    path('pj-add/', CadastroEmpresa.as_view(), name='empresa-cadastro'),
    path('pj-edit/<int:pk>/', EditarEmpresa.as_view(), name='empresa-edit'),
    path('pj-loc/', BuscaEmpresa.as_view(), name='empresa-busca'),
    path('pj-del/<int:pk>/', DeleteEmpresa, name='empresa-delete'),


    path('agenda-tel/', Agenda.as_view(), name='agenda-telefonica'),
]
