from django.shortcuts import render

from posts.forms import AddPostContentForm, PostInformationForm
from posts.services import add_post_content_to_db, add_post_info_to_db


def homePageView(request):
    return render(request, 'pages/index.html')


def addNewPostView(request):
    if request.method == 'POST':
        add_post_info_to_db(request.POST)
    return render(request, 'pages/add_post.html', {
        'post_information_form': PostInformationForm,
        'add_content_form': AddPostContentForm
    })


def handle404Error(request):
    pass
