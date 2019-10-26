from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post, Vote
from .helper import get_postdetails
from django.db.models import Count
from django.views import View


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
			setattr(request, 'user', user)
			request.session['user_id'] = user.id
			return redirect('posts')
		context['error'] = 'Invalid credentials'
		return render(request, 'login.html', context)
	return render(request, 'login.html', context)

def profile(request):
	context = {
		'posts' : None
	}
	user_id = request.session['user_id']
	if request.method == 'POST':
		if 'new_post' in request.POST:
			post_title = request.POST.get('post_title')
			post_content = request.POST.get('post_content')
			post = Post(title=post_title, content=post_content, createdby_id=userid)
			post.save()
		print(request.POST)
	context['posts'] = get_postdetails(user_id)
	return render(request, 'profile.html', context)

# class PostList(ListView):
# 	template_name = 'post/post.html'

# 	def get_queryset(self):
# 		return Post.objects.all()

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		posts = Post.objects.prefetch_related('votes').annotate(Count('votes', distinct=True)).values(
# 			'title', 'content', 'votes__count')
# 		for post in posts:
# 			context['title'] = post['title']
# 			context['content'] = post['content']
# 			context['votes'] = post['votes__count']
# 		return context

class PostView(View):
	template_name = 'post/post.html'
  
	def get(self, request, *args, **kwargs):
		context = {
		 'posts' : []
		}
		posts = Post.objects.prefetch_related('votes').annotate(Count('votes', distinct=True)).values(
			'title', 'content', 'votes__count')
		for post in posts:
			context['posts'].append({
				'title' : post['title'],
				'content' : post['content'],
				'votes' : post['votes__count']
			})
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		user_id = request.session['user_id']
		post_title = request.POST.get('post_title')
		post_content = request.POST.get('post_content')
		post = Post(title=post_title, content=post_content, createdby_id=user_id)
		post.save()
		return redirect('posts')


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