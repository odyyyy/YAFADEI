from django.contrib import admin
from posts.models import Posts


class PostsAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Posts, PostsAdmin)
