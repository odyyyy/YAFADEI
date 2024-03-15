from django.contrib import admin
from django.urls import path, include

from posts.views import PostPageView

urlpatterns = [
    path('<slug:slug>/', PostPageView.as_view(), name="post_page"),
]
