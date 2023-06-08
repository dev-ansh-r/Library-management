from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home',views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('search_books', views.search_books, name="search_books"),
]