from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post, Vote

def login(request):
	# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
	# user.save()
	# user = UserSystem.objects.get(user_id=5)
	# post = Post(title='django', content='programming language', createdby_id=1)
	# post.save()
	post = Post.objects.get(id=3)
	vote = Vote(votedby_id=2)
	vote.save()
	post.votes.add(vote)
	print(post.votes.all())
	return HttpResponse('Success')