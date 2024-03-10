from django.urls import path

from posts.views import addNewPostView

urlpatterns = [
    path('', addNewPostView)
]
