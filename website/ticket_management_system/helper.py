from .models import Post, Vote
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Count


def uservoted(votes, username):
	for vote in votes:
		if str(vote.votedby) == str(username):
			return True
		return False

def get_postdetails(user_id):
	print(len(connection.queries))
	posts = Post.objects.prefetch_related('votes').annotate(Count('votes', distinct=True)
		).values(
		'title', 'content', 'votes__count')
	post_details = []
	for post in posts:
		post_details.append({
			'title': post['title'],
			'content': post['content'],
			'votes': post['votes__count'],
		})
	print(len(connection.queries))
	return post_details