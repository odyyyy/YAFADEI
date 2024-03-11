from django.shortcuts import render, redirect

from posts.forms import AddPostForm
from posts.services import add_post_info_to_db, get_posts_list_from_db, get_post_from_db


def homepage_view(request):
    return render(request, 'pages/index.html')


def add_new_post_view(request):
    if request.method == 'POST':
        add_post_info_to_db(request)
        return redirect('homepage')
    return render(request, 'pages/add_post.html', {
        'form': AddPostForm
    })


def show_posts_view(request):
    posts_list = get_posts_list_from_db()
    return render(request, 'pages/posts.html', {"posts_list": posts_list})


def post_page_view(request, post_slug: str):
    post = get_post_from_db(post_slug)
    return render(request, 'pages/post_page.html', {'post': post})


def handle404Error(request):
    pass
