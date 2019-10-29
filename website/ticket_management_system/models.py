from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
	title = models.TextField()
	content = models.TextField()
	createdby = models.ForeignKey(User, on_delete=models.CASCADE)
	votes = models.ManyToManyField('Vote')
	comments = models.ManyToManyField('Comment')

	def __repr__(self):
		return self.title

class Vote(models.Model):
	votedby = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
	content = models.TextField(blank=True)
	commentedby = models.ForeignKey(User, on_delete=models.CASCADE)