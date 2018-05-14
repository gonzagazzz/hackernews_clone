from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Article(models.Model):
	title = models.CharField(max_length=300)
	link = models.CharField(max_length=300)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	upvotes = models.IntegerField()

	def __str__(self):
		return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	message = models.CharField(max_length=5000)
	authorName = models.CharField(max_length=60)

	def __str__(self):
		return self.author