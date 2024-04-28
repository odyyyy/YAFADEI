from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegisterForm


class UserViewTests(TestCase):
    def test_register_user_view(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/users/register.html")

    def test_registration_form(self):
        data = {
            "username": "testuser",
            "email": "testemail@mail.ru",
            "password1": "Fas0dckv8fd1",
            "password2": "Fas0dckv8fd1",
        }

        form = UserRegisterForm(data)

        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_login_user_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/users/login.html")

    # def test_login_user_form(self):
    #     User.objects.create(username="testuser", password="Fas0dckv8fd1")
    #     data = {"username": "testuser", "password": "Fas0dckv8fd1"}
    #
    #     form = LoginUserForm()
    #     form.username = data["username"]
    #     form.password = data["password"]
    #
    #
    #     self.assertTrue(form.is_valid())
