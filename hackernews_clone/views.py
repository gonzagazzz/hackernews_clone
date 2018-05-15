from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from posts.models import Article, Comment
from django.core.paginator import Paginator

def homepage(request):
	articles = Article.objects.all()
	#PAGINATOR
	page = request.GET.get('page', 1)
	paginator = Paginator(articles, 30)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	
	comments=[]
	for article in articles:
		comments.append(Comment.objects.filter(article=article).count())
		if article.get_users_upvoted().count(request.user.username) > 0:
			article.upvoted = True;
			article.save()
	return render(request, "index.html", {"articles": articles, "comments": comments})	

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')

def new(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('http://yahoo.com')
    else:
        return HttpResponseRedirect('http://google.com')