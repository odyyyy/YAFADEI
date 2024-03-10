from django.db import models
from tinymce import models as tinymce_models


# Create your models here.

class PostCards(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок поста")
    # description = models.TextField(blank=True, verbose_name="Описание")
    # TODO: Добавить картинку по умолчанию
    img = models.ImageField(upload_to='photos/%Y/%m/%d/',
                            default='media/svg/no_image_avaliable.svg',
                            verbose_name="Фото")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    karma = models.IntegerField(default=0, verbose_name='Карма')
    published_time = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')

    def __str__(self):
        return self.title


class Posts(models.Model):
    slug = models.OneToOneField(PostCards, on_delete=models.CASCADE)
    content = tinymce_models.HTMLField()
