from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
	path('', views.index, name='index'),
 	path('login', views.login, name='login'),
 	path('docs/', views.docs, name='docs'),
 	path('signup/', views.signup, name='signup'),
 	path('developer/', views.dev, name='signup'),    
]
