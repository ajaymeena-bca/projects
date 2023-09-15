from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
      path('', views.log_in, name='login'),
      path('login/', views.log_in, name='login'),
      path('signup/', views.signUp, name='signup'),
]
