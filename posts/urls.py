from django.urls import path

from posts.views import PostPageView

urlpatterns = [
    path("<slug:slug>/", PostPageView.as_view(), name="post_page"),
]
