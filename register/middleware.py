from django.contrib.auth import get_user_model
from django.conf import settings


class AutoLoginMiddleware:
    """
    Middleware para autenticar automaticamente como usuário admin
    (ou outro) no ambiente de desenvolvimento.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.User = get_user_model()

    def __call__(self, request):
        if settings.DEBUG and not request.user.is_authenticated:
            try:
                # Troque 'admin' pelo username que desejar
                user = self.User.objects.get(username='admin')
                # Força o login do usuário
                request.user = user
                # Também atribui no backend (requer para Django autenticar direito)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
            except self.User.DoesNotExist:
                pass

        response = self.get_response(request)
        return response
