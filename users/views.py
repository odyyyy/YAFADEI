from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, UserRegisterForm


class RegisterUser(CreateView):
    """Вью для страницы регистрации"""

    form_class = UserRegisterForm
    template_name = "pages/users/register.html"
    success_url = reverse_lazy("login")


class LoginUser(LoginView):
    """Вью для страницы авторизации"""

    form_class = LoginUserForm
    template_name = "pages/users/login.html"

    def get_success_url(self):
        return reverse_lazy("homepage")
