from django.contrib import admin
from django.urls import path, include

from posts.views import homepage_view, add_new_post_view, show_posts_view, post_page_view

urlpatterns = [
    path('<slug:post_slug>/', post_page_view, name="category-name"),
]
