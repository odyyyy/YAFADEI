from django.contrib import admin
from django.urls import path, include

from posts.views import homePageView, addNewPostView, showPostsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', homePageView),
    path('new/', addNewPostView),
    path('posts/', showPostsView),
]
