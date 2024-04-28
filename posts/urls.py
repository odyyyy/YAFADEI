from django.urls import path

from posts import views as posts_view

urlpatterns = [
    path("<slug:slug>/", posts_view.PostPageView.as_view(), name="post_page"),
    path("like/<slug:slug>/", posts_view.post_like_view, name="post_like"),
    path(
        "dislike/<slug:slug>/",
        posts_view.post_dislike_view,
        name="post_dislike",
    ),
]
