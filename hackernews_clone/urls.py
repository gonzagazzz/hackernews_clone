"""hackernews_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from login.views import UserFormView
from login.views import LoginFormView
from django.contrib.auth.views import logout
from django.conf.urls import url
from django.conf import settings
from posts.views import PostFormView, CommentFormView, upvote, downvote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.homepage),
    path('register/', UserFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('new/', PostFormView.as_view()),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}),
    url(r'^comments/(?P<article_id>[0-9]+)/$', CommentFormView.as_view(), name='comments'),
    url(r'^upvote/(?P<article_id>[0-9]+)/$', upvote, name='upvote'),
    url(r'^downvote/(?P<article_id>[0-9]+)/$', downvote, name='downvote'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)