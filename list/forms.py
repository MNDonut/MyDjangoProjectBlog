from django.forms import ModelForm, TextInput
from .models import Post

class PostFrom(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"