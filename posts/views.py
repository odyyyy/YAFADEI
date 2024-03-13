from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from YAFADEI.settings import LOGIN_URL
from posts.forms import AddPostForm
from posts.services import add_post_info_to_db, get_posts_list_from_db, get_post_from_db


def homepage_view(request):
    return render(request, 'pages/index.html')

@login_required(login_url=LOGIN_URL)
def add_new_post_view(request):
    if request.method == 'POST':
        add_post_info_to_db(request)
        return redirect('homepage')
    return render(request, 'pages/posts/add_post.html', {
        'form': AddPostForm
    })


def show_posts_view(request):
    posts_list = get_posts_list_from_db()
    return render(request, 'pages/posts/posts.html', {"posts_list": posts_list})


def post_page_view(request, post_slug: str):
    post = get_post_from_db(post_slug)
    return render(request, 'pages/posts/post_page.html', {'post': post})


def handle404Error(request, exception):
    return render(request, 'pages/errors/404.html')

def handle500Error(request):
    return render(request, 'pages/errors/500.html')
