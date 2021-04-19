from django.forms import ModelForm, TextInput, Textarea
from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'title': TextInput(attrs={
                'class': 'create-title', 
                'placeholder': 'Enter title'}),
            'description': Textarea(attrs={
                'class': 'create-description',
                'placeholder': 'Your description for this post'})
        }