from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils.text import slugify

from users.models import User

from .models import Posts


class PostsServiceTests(TestCase):
    pass


class PostsViewTests(TestCase):
    """Модульное тестирование вью"""

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )
        self.post = Posts.objects.create(
            title="Test Post",
            content="Test Content",
            slug=slugify("Test Post"),
            user=self.user,
        )

    def test_homepage(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/index.html")

    def test_post_page(self):
        post = Posts.objects.create(
            title="Test Post",
            slug="test-post",
            content="Test content",
            user_id=1,
        )

        response = self.client.get(
            reverse("post_page", kwargs={"slug": post.slug})
        )
        self.assertTemplateUsed(response, "pages/posts/post_page.html")
        self.assertEqual(response.status_code, 200)
