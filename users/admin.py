from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import FavoritePost, Subscription, User


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )


class SubscriptionAdmin(admin.ModelAdmin):
    pass


class FavoritePostAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(FavoritePost, FavoritePostAdmin)
