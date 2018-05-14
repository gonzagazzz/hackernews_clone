from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from posts.models import Article

def homepage(request):
	data = Article.objects.all()
	stu = {
	    "articles": data
	}
	return render(request, "index.html", stu)	

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')

def new(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('http://yahoo.com')
    else:
        return HttpResponseRedirect('http://google.com')