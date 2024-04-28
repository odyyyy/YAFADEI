from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

from users.views import LoginUser, RegisterUser

app_name = "users"

urlpatterns = [
    path("signup/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # ИЗМЕНЕНИЕ ПАРОЛЯ
    path(
        "password-change/",
        PasswordChangeView.as_view(
            template_name="pages/users/password_change_form.html",
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(
            template_name="pages/users/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # СБРОС ПАРОЛЯ
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="pages/users/password_reset_form.html",
            email_template_name="pages/users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="pages/users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="pages/users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="pages/users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
