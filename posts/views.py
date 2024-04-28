from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from posts.forms import AddPostForm
from posts.models import Posts
from posts.services import add_post_info_to_db, get_posts_list_from_db
from users.models import FavoritePost
from YAFADEI.settings import LOGIN_URL


def homepage_view(request):
    """Вью для главной страницы сайта"""
    return render(request, "pages/index.html")


@login_required(login_url=LOGIN_URL)
def get_users_favorite_posts_view(request):
    """Вью для страницы с избранными постами"""
    user_id = request.user.id

    user_favorite_posts = FavoritePost.objects.filter(user=user_id)

    return render(
        request,
        "pages/posts/favorite_posts.html",
        {"posts": user_favorite_posts, "quantity": len(user_favorite_posts)},
    )


@login_required(login_url=LOGIN_URL)
def add_new_post_view(request):
    """Вью для страницы добавления новых постов"""
    if request.method == "POST":
        request_data = {
            "title": request.POST.get("title"),
            "content": request.POST.get("content"),
            "user": request.user,
            "img": request.FILES.get("img"),
        }

        add_post_info_to_db(request_data)
        return redirect("posts_page")
    return render(request, "pages/posts/add_post.html", {"form": AddPostForm})


class AllPostsPageView(ListView):
    """Вью для страницы со списком всех постов"""

    template_name = "pages/posts/posts.html"
    context_object_name = "posts_list"
    queryset = get_posts_list_from_db()


class PostPageView(DetailView):
    """Вью для страницы поста"""

    model = Posts
    template_name = "pages/posts/post_page.html"
    context_object_name = "post"


@login_required(login_url=LOGIN_URL)
def post_like_view(request, slug):
    """Вью для лайка поста"""
    post = Posts.objects.get(slug=slug)
    user = request.user

    if post.like.filter(id=user.id).exists():
        post.like.remove(user)
        if post.dislike.filter(id=user.id).exists():
            post.dislike.add(user)
    else:
        if post.dislike.filter(id=user.id).exists():
            post.dislike.remove(user)
        post.like.add(user)

    return redirect("posts_page")


@login_required(login_url=LOGIN_URL)
def post_dislike_view(request, slug):
    """Вью для дизлайка поста"""
    post = Posts.objects.get(slug=slug)
    user = request.user

    if post.dislike.filter(id=user.id).exists():
        post.dislike.remove(user)
    else:
        if post.like.filter(id=user.id).exists():
            post.like.remove(user)
        post.dislike.add(user)

    return redirect("posts_page")


def get_likes_count_view(request, slug):
    post = Posts.objects.get(slug=slug)
    likes_count = post.like.count()
    return JsonResponse({"likes_count": likes_count})


def handle404Error(request, exception):
    """Вью для обработки ошибки 404"""
    return render(request, "pages/errors/404.html")


def handle500Error(request):
    """Вью для обработки ошибки 500"""
    return render(request, "pages/errors/500.html")
