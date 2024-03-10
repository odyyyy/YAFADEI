# For business logic :)
import random

from django.http import QueryDict
from django.utils.text import slugify

from posts.models import Posts


def generate_post_slug(title: str):
    post_generated_id = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return slugify(title) + '-' + post_generated_id


def add_post_info_to_db(req):
    """ Общая функция добавляющая всю информацию о созданном посте в БД """

    post_title = req.POST.get('title')
    post_image = req.FILES.get('img')
    post_content = req.POST.get('content')
    post_user = req.user
    post_slug = generate_post_slug(post_title)


    if post_image != '':
        Posts.objects.create(slug=post_slug, title=post_title, img=post_image, content=post_content, user=post_user)
    else:
        Posts.objects.create(slug=post_slug, title=post_title, content=post_content, user=post_user)
