from django.contrib.flatpages.models import FlatPage
from django import forms
from tinymce.widgets import TinyMCE

from posts.models import Posts, PostCards


class PostInformationForm(forms.ModelForm):
    class Meta:
        model = PostCards
        fields = ('title', 'img',)


class AddPostContentForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('content',)
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30, "content_language": 'ru_RU'},  content_language='ru_RU')}
