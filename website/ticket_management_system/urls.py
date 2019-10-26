from django.urls import path
from . import views
from .views import PostView

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('profile/', views.profile, name='profile'),
	path('posts/', PostView.as_view(), name='posts')
]