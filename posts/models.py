from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import json

class Article(models.Model):
	title = models.CharField(max_length=300)
	link = models.CharField(max_length=300)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	upvotes = models.IntegerField()
	users_upvoted = models.CharField(max_length=100000)
	upvoted = False
	visible = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def set_users_upvoted(self, x):
		self.users_upvoted = json.dumps(x)

	def get_users_upvoted(self):
		return json.loads(self.users_upvoted)

	def count_comments(self):
		return Comment.objects.filter(article=self).count()

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	message = models.CharField(max_length=5000)
	authorName = models.CharField(max_length=60)

	def __str__(self):
		return self.message