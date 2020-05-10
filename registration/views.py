from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = 'registration/login.html'


class Logout(LogoutView):
    template_name = 'registration/logout.html'
