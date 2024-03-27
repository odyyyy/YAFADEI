from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class User(AbstractUser):
    favorite_posts = models.JSONField(default=list)
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
