from django.db.models import QuerySet
from django.utils.text import slugify

from django.test import TestCase, RequestFactory
from django.urls import reverse

from users.models import User
from .models import Posts


class PostsServiceTests(TestCase):
    pass


class PostsViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Posts.objects.create(title='Test Post', content='Test Content', slug=slugify('Test Post'),
                                         user=self.user)
        self.posts = [Posts("test", "content", "test-1", "admin"),
                      Posts("test1", "content1", "test-2", "admin"),
                      Posts("test2", "content2", "test-3", "admin"),
                      Posts("test3", "content3", "test-4", "admin")
                      ]

    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_post_page_not_found(self):
        response = self.client.get(reverse('post_page'), 'not-found-slug')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'pages/posts/post_page.html')
