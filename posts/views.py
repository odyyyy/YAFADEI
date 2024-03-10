from django.shortcuts import render

from posts.forms import AddPostForm
from posts.services import add_post_info_to_db


def homePageView(request):
    return render(request, 'pages/index.html')


def addNewPostView(request):
    if request.method == 'POST':
        add_post_info_to_db(request)
    return render(request, 'pages/add_post.html', {
        'form': AddPostForm
    })


def handle404Error(request):
    pass
