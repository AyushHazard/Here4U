from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('', views.home, name = "client-home"),
    path('about/',views.about, name="client-about"),
    path('talk/',views.talk,name = "talk-to-counsellor"),
    path('signup/',views.signup,name="sign-up"),
    path('accounts/login',views.login,name='login'),
]