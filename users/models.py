from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

from posts.models import Posts


class User(AbstractUser):
    """Расширенная модель пользователя"""

    groups = models.ManyToManyField(
        "auth.Group", related_name="custom_user_set"
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions"
    )

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Подписчик"
    )
    subscribed_to = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Подписан на"
    )


class FavoritePost(models.Model):
    user = models.ForeignKey(
        User, related_name="favorite_posts", on_delete=models.CASCADE
    )
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
