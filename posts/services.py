# For business logic :)
import random

from django.http import QueryDict
from django.utils.text import slugify

from posts.models import Posts, PostCards


def generate_post_slug(title: str):
    post_generated_id = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return slugify(title) + '-' + post_generated_id


def add_post_info_to_db(post_data: QueryDict):
    """ Общая функция добавляющая всю информацию о созданном посте в БД """
    print(post_data)
    post_title = post_data.get('title')
    post_image = post_data.get('img')
    post_slug = generate_post_slug(post_title)
    post_content = post_data.get('content')

    add_post_card_info_to_db(post_title, post_image, post_slug)
    add_post_content_to_db(post_content, post_slug)


def add_post_card_info_to_db(post_title: str, post_image: str, post_slug: str):
    """ Функция добавляющая информацию для карточки поста в БД """

    if post_image != '':
        PostCards.objects.create(title=post_title, img=post_image, slug=post_slug)
    else:
        PostCards.objects.create(title=post_title, slug=post_slug)


def add_post_content_to_db(post_content: str, post_slug: str):
    """ Общая функция добавляющая контент статьи в БД """
    post_info = PostCards.objects.get(slug=post_slug)
    Posts.objects.create(slug=post_info, content=post_content)
