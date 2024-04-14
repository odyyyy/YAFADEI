from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.utils.text import slugify

from users.models import User

from .models import Posts
from .services import add_post_info_to_db


class PostsServiceTests(TestCase):
    """Тестирование логики добавления поста в БД"""

    def test_POST_new_post_in_db(self):

        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )

        add_post_info_to_db(
            {
                "title": "Test Post",
                "content": "Test Content",
                "user": self.user,
                "img": None,
            }
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


class AddNewPostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )

    def test_add_new_post_view_get(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("new_post"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/posts/add_post.html")

    def test_add_new_post_view_post(self):
        self.client.login(username="testuser", password="12345")
        post_data = {
            "title": "Test Post",
            "content": "Test Content",
            "img": "",
        }
        response = self.client.post(reverse("new_post"), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Posts.objects.filter(title="Test Post").exists())

    def test_add_new_post_view_post_unauthenticated(self):
        response = self.client.post(reverse("new_post"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/new/")
