from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf.urls.static import static
from posts.views import homepage_view, add_new_post_view, show_posts_view, handle404Error, handle500Error
from users.views import RegisterUser, LoginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', homepage_view, name='homepage'),
    path('new/', add_new_post_view, name='new_post'),
    path('posts/', show_posts_view, name='show_post'),
    path('post/', include('posts.urls')),
    path('signup/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

handler404 = handle404Error
handler500 = handle500Error

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
