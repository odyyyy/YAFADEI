from django import forms
from tinymce.widgets import TinyMCE

from posts.models import Posts


class AddPostForm(forms.ModelForm):
    """Форма для добавление нового поста"""

    class Meta:
        model = Posts
        fields = ("title", "img", "content")
        widgets = {
            "content": TinyMCE(
                attrs={"cols": 80, "rows": 30, "content_language": "ru_RU"},
                content_language="ru_RU",
            )
        }
