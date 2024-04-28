from django.conf import settings
from django.db import models
from django.utils.timezone import now
from tinymce import models as tinymce_models


class Posts(models.Model):
    """Модель для хранения данных о постах"""

    title = models.CharField(max_length=255, verbose_name="Заголовок поста")
    img = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default="/svg/no_image_avaliable.svg",
        verbose_name="Фото",
    )
    slug = models.SlugField(
        max_length=255, db_index=True, unique=True, verbose_name="URL"
    )
    # karma = models.IntegerField(default=0, verbose_name="Карма")
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="likes", verbose_name="Лайки"
    )
    dislike = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dislikes",
        verbose_name="Дизлайки",
    )
    published_time = models.DateTimeField(
        default=now, verbose_name="Время публикации"
    )
    content = tinymce_models.HTMLField(verbose_name="Содержание статьи")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, **kwargs):
        """При сохранении записи добавляем id в конец слага если он уже не добавлен
        (при добавления постов через админку)"""
        super(Posts, self).save()
        if not self.slug.endswith("-" + str(self.id)):
            self.slug += "-" + str(self.id)
            super(Posts, self).save()

    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Посты"
        ordering = ["-published_time"]

    def __str__(self):
        return f"Пост: {self.title}"
