from django.urls import path
from .views import Pf_DetailView, Pf_ListView, Pf_CreateView, Pf_UpdateView, Pf_DeleteView
from .views import Pj_DetailView, Pj_ListView, Pj_CreateView, Pj_UpdateView, Pj_DeleteView
from .views import Log_View, Agenda_ListView


urlpatterns = [
    # Pessoa
    path('pf/', Pf_ListView.as_view(), name='pessoa-busca'),
    path('pf/add/', Pf_CreateView.as_view(), name='pessoa-cadastro'),
    path('pf/<int:pk>/', Pf_DetailView.as_view(), name='pessoa-detail'),
    path('pf/<int:pk>/edit/', Pf_UpdateView.as_view(), name='pessoa-edit'),
    path('pf/<int:pk>/del/', Pf_DeleteView.as_view(), name='pessoa-delete'),
    # Empresa
    path('pj/', Pj_ListView.as_view(), name='empresa-busca'),
    path('pj/add/', Pj_CreateView.as_view(), name='empresa-cadastro'),
    path('pj/<int:pk>/', Pj_DetailView.as_view(), name='empresa-detail'),
    path('pj/<int:pk>/edit/', Pj_UpdateView.as_view(), name='empresa-edit'),
    path('pj/<int:pk>/del/', Pj_DeleteView.as_view(), name='empresa-delete'),
    # Utilitarios
    path('agenda/', Agenda_ListView.as_view(), name='agenda-telefonica'),
    path('cad/<int:pk>/log/', Log_View.as_view(), name='log-cadastro'),
]
