from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from YAFADEI.settings import LOGIN_URL
from posts.forms import AddPostForm
from posts.models import Posts
from posts.services import add_post_info_to_db, get_posts_list_from_db, get_post_from_db


def homepage_view(request):
    return render(request, 'pages/index.html')


@login_required(login_url=LOGIN_URL)
def add_new_post_view(request):
    if request.method == 'POST':
        add_post_info_to_db(request)
        return redirect('posts_page')
    return render(request, 'pages/posts/add_post.html', {
        'form': AddPostForm
    })


class AllPostsPageView(ListView):
    template_name = 'pages/posts/posts.html'
    context_object_name = 'posts_list'
    queryset = get_posts_list_from_db()


class PostPageView(DetailView):
    model = Posts
    template_name = 'pages/posts/post_page.html'
    context_object_name = 'post'


def handle404Error(request, exception):
    return render(request, 'pages/errors/404.html')


def handle500Error(request):
    return render(request, 'pages/errors/500.html')
