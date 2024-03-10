from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок поста")
    description = models.TextField(blank=True, verbose_name="Описание")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    published_time = models.DateTimeField(auto_now_add=True,verbose_name='Время публикации')

    def __str__(self):
        return self.title

