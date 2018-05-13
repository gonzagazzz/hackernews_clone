from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'index.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')

def new(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('http://yahoo.com')
    else:
        return HttpResponseRedirect('http://google.com')