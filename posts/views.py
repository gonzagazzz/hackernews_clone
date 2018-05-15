from django.shortcuts import render
from .forms import PostForm
from django.views.generic import View
from posts.models import Article
from django.shortcuts import redirect
from posts.forms import CommentForm
from posts.models import Comment

class PostFormView(View):
    form_class = PostForm
    template_name = 'post_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # authenticate user
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
        	temp = form.save(commit=False)
        	if request.user.is_authenticated:
        		temp.author = request.user
        	temp.upvotes = 0
        	lst = []
        	temp.set_users_upvoted(lst)
        	temp.save()
        	return redirect('../')

        return render(request, self.template_name, {'form': form})

class CommentFormView(View):
    form_class = CommentForm
    template_name = 'post_comments.html'

    # display a blank form
    def get(self, request, article_id):
        form = self.form_class(None)
        try:
        	article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
        	raise Http404("Article does not exist")

        comments = Comment.objects.filter(article=article)
        return render(request, self.template_name, {'form': form, "comments": comments, "article": article})

    # authenticate user
    def post(self, request, article_id):
        form = self.form_class(request.POST)
        try:
        	article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
        	raise Http404("Article does not exist")

        if form.is_valid():
        	temp = form.save(commit=False)
        	if request.user.is_authenticated:
        		temp.author = request.user
        	temp.article = article
        	temp.save()
        	return redirect('../..')

        return render(request, self.template_name, {'form': form})

def upvote(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		users_upvoted = article.get_users_upvoted()
		if users_upvoted.count(request.user.username) == 0:
			article.upvotes+=1
			users_upvoted.append(request.user.username)
			article.set_users_upvoted(users_upvoted)
			article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect('../..')

def downvote(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		users_upvoted = article.get_users_upvoted()
		if users_upvoted.count(request.user.username) > 0:
			article.upvotes -= 1
			users_upvoted.remove(request.user.username)
			article.set_users_upvoted(users_upvoted)
			article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect('../..')

def hide(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		if article.visible is True:
			article.visible = False
			article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect('../..')