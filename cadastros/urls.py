from django.urls import path
from .views import CadastroPessoa, EditarPessoa, BuscaPessoa, DeletePessoa
from .views import CadastroEmpresa, EditarEmpresa, BuscaEmpresa, DeleteEmpresa

urlpatterns = [
    path('pessoa/', CadastroPessoa.as_view(), name='pessoa-cadastro'),
    path('pessoa/edit/<int:pk>', EditarPessoa.as_view(), name='pessoa-edit'),
    path('pessoa/busca/', BuscaPessoa.as_view(), name='pessoa-busca'),
    path('pessoa/delete/<int:pk>', DeletePessoa.as_view(), name='pessoa-delete'),

    path('empresa/', CadastroEmpresa.as_view(), name='empresa-cadastro'),
    path('empresa/edit/<int:pk>', EditarEmpresa.as_view(), name='empresa-edit'),
    path('empresa/busca/', BuscaEmpresa.as_view(), name='empresa-busca'),
    path('empresa/delete/<int:pk>', DeleteEmpresa.as_view(), name='empresa-delete'),
]
