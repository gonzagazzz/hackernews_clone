from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=250)
	message = models.CharField(max_length=5000)
	author = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	message = models.CharField(max_length=1000)
	author = models.CharField(max_length=50)

	def __str__(self):
		return self.title + self.id