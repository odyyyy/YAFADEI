from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils.text import slugify

from users.models import User

from .models import Posts
from .services import add_post_info_to_db


class PostsServiceTests(TestCase):
    """Тестирование логики добавления поста в БД"""

    def test_POST_new_post_in_db(self):

        add_post_info_to_db(
            title="Test Post",
            content="Test Content",
            slug=slugify("Test Post"),
            user_id=1,
        )
        self.assertEqual(Posts.objects.count(), 1)


class HomePageTests(TestCase):
    def test_home_page_template_use(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/index.html")


class PostsViewTests(TestCase):
    """Модульное тестирование вьюшки отдающей все посты"""

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

    def test_show_all_posts_view(self):
        response = self.client.get(reverse("posts_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/posts/posts.html")

    def test_add_new_post_view(self):
        response = self.client.get(reverse("add_new_post"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/posts/add_post.html")
