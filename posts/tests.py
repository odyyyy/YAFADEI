from django.utils.text import slugify

from django.test import TestCase, RequestFactory
from django.urls import reverse

from users.models import User
from .models import Posts


class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Posts.objects.create(title='Test Post', content='Test Content', slug=slugify('Test Post'), user=self.user)

    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

