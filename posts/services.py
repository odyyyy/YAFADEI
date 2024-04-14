# For business logic :)
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

from posts.models import Posts


def get_posts_list_from_db():
    """Функция для получения всех постов, отсортированных по времени"""
    return list(Posts.objects.values().order_by("-published_time"))


def get_post_from_db(post_slug: str):
    """Функция получения поста из БД по слагу"""
    post = get_object_or_404(Posts, slug=post_slug)
    return post


def add_post_info_to_db(request_data):
    """Общая функция добавляющая всю информацию о созданном посте в БД"""

    post_title = request_data["title"]
    post_image = request_data["img"]
    post_content = request_data["content"]
    post_user = request_data["user"]

    post_slug = generate_post_slug(post_title, post_user)
    print(post_image, post_image is not None)
    if post_image is not None:
        Posts.objects.create(
            slug=post_slug,
            title=post_title,
            img=post_image,
            content=post_content,
            user=post_user,
        )
    else:
        Posts.objects.create(
            slug=post_slug,
            title=post_title,
            content=post_content,
            user=post_user,
        )


def generate_post_slug(title: str, user_id: int):
    """Функция для генерация слага по заголовку поста"""
    # post_generated_id = "".join([str(random.randint(0, 9)) for _ in range(5)])
    return slugify(title) + "-" + str(user_id)
