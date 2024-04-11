from django.contrib.auth.models import AbstractUser
from django.db import models

from posts.models import Posts


class User(AbstractUser):
    """Расширенная модель пользователя"""

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriber",
        verbose_name="Подписчик",
    )
    subscribed_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscribed_to",
        verbose_name="Подписан на",
    )


class FavoritePost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_posts"
    )
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
