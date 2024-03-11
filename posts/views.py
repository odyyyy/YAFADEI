from django.shortcuts import render

from posts.forms import AddPostForm
from posts.services import add_post_info_to_db, get_posts_list_from_db


def homePageView(request):
    return render(request, 'pages/index.html')


def addNewPostView(request):
    if request.method == 'POST':
        add_post_info_to_db(request)
    return render(request, 'pages/add_post.html', {
        'form': AddPostForm
    })


def showPostsView(request):
    posts_list = get_posts_list_from_db()
    print(posts_list)
    return render(request, 'pages/posts.html', {"posts_list": posts_list})


def handle404Error(request):
    pass
