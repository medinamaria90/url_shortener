from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.ShorterlinkCreateAPIView.as_view()),
    path('list/', views.ShorterlinkListAPIView.as_view()),
    path('<str:short_link>/update/', views.ShorterlinkUpdateView.as_view(), name='product-edit'),
    path('<str:short_link>/delete/', views.ShorterlinkDeleteView.as_view(), name='product-delete'),
    path('<str:short_link>/', views.ShorterlinkDetailAPIView.as_view(), name='product-detail'),
]
