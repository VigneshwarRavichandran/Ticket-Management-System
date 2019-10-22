from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Post, Vote

def register(request):
	context = {
		'error' : None,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
			return redirect(login)
		except:
			context['error'] = 'User already exsists'
	return render(request, 'register.html', context)

def login(request):
	context = {
		'error' : None,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			# return redirect(profile, user.id, user)
			return HttpResponse('Success')
		context['error'] = 'Invalid credentials'
		return render(request, 'login.html', context)
	return render(request, 'login.html', context)

# 	# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
# 	# user.save()
# 	# user = UserSystem.objects.get(user_id=5)
# 	# post = Post(title='django', content='programming language', createdby_id=1)
# 	# post.save()
# 	post = Post.objects.get(id=3)
# 	vote = Vote(votedby_id=2)
# 	vote.save()
# 	post.votes.add(vote)
# 	print(post.votes.all())
# 	return HttpResponse('Success')