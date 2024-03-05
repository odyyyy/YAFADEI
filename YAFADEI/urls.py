from django.contrib import admin
from django.urls import path

from posts.views import homePageView, handle404Error

handler404 = handle404Error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePageView)
]
