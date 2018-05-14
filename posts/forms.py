from django.forms import ModelForm
from .models import Article, Comment

class PostForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'link']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']