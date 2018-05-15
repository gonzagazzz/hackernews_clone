from django.forms import ModelForm
from .models import Article, Comment
from django import forms

class PostForm(ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
	link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Link'}))

	class Meta:
		model = Article
		fields = ['title', 'link']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']