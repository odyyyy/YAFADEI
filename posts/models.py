import random
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from tinymce import models as tinymce_models




class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок поста")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/',
                            default='/svg/no_image_avaliable.svg',
                            verbose_name="Фото")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    karma = models.IntegerField(default=0, verbose_name='Карма')
    published_time = models.DateTimeField(default=datetime.now(), verbose_name='Время публикации')
    content = tinymce_models.HTMLField(verbose_name='Содержание статьи')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Посты"
        ordering = ['published_time']


    def __str__(self):
        return f"Пост: {self.title}"


