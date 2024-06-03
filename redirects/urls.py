from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [   
  	path('<str:short_link>/', views.url_redirection, name='url_redirection'),
]
