from django.urls import path
from .views import Pf_DetailView, Pf_ListView, Pf_CreateView, Pf_UpdateView, Pf_DeleteView
from .views import Pj_DetailView, Pj_ListView, Pj_CreateView, Pj_UpdateView, Pj_DeleteView
from .views import Pf_Log_View, Pj_Log_View, Contacts_ListView


app_name = 'register'


urlpatterns = [
    # Pessoa
    path('pf/', Pf_ListView.as_view(), name='person_'),
    path('pf/0/adicionar/', Pf_CreateView.as_view(), name='person_add'),
    path('pf/<int:pk>/visualizar/', Pf_DetailView.as_view(), name='person_detail'),
    path('pf/<int:pk>/editar/', Pf_UpdateView.as_view(), name='person_change'),
    path('pf/<int:pk>/deletar/', Pf_DeleteView.as_view(), name='person_delete'),
    path('pf/<int:pk>/log/', Pf_Log_View.as_view(), name='person_log'),
    # Empresa
    path('pj/', Pj_ListView.as_view(), name='enterprise_'),
    path('pj/0/adicionar/', Pj_CreateView.as_view(), name='enterprise_add'),
    path('pj/<int:pk>/visualizar/', Pj_DetailView.as_view(), name='enterprise_detail'),
    path('pj/<int:pk>/editar/', Pj_UpdateView.as_view(), name='enterprise_edit'),
    path('pj/<int:pk>/deletar/', Pj_DeleteView.as_view(), name='enterprise_delete'),
    path('pj/<int:pk>/log/', Pj_Log_View.as_view(), name='enterprise_log'),
    # Utilitarios
    path('agenda/', Contacts_ListView.as_view(), name='contacts_'),
]
