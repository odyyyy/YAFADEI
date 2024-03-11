from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from posts.views import homepage_view, add_new_post_view, show_posts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', homepage_view, name='homepage'),
    path('new/', add_new_post_view, name='new_post'),
    path('posts/', show_posts_view, name='show_post'),
    path('post/', include('posts.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
