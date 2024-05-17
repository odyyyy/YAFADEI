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
    path(
        "edit/<slug:slug>/", posts_view.EditPostView.as_view(), name="edit_post"
    ),
    path(
        "delete/<slug:slug>/",
        posts_view.DeletePostIView.as_view(),
        name="delete_post",
    ),
    path("favorite/<slug:slug>/", posts_view.favorite_view, name="favorite"),
]
