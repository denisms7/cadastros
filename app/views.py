from django.views.generic import DetailView
from django.contrib.auth.models import User


class UsuarioDetailView(DetailView):
    model = User
    template_name = 'usuarios/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['groups'] = user.groups.all()
        context['user_permissions'] = user.user_permissions.all()
        context['group_permissions'] = user.get_group_permissions()  # opcional
        return context
