from django.urls import path
from . import views
from django.shortcuts import render, redirect

# from counsellor.urls import

urlpatterns = [
    path('', views.home, name = "client-home"),
    path('about/',views.about, name="client-about"),
    path('talk/',views.talk,name = "talk-to-counsellor"),
    path('signup/',views.signup,name="sign-up"),
    path('update-profile/',views.updateProfile,name="update-profile"),
    # path('accounts/login/',views.login,name='login'),
    # path('accounts/logout/',views.logout,name='log-out'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('pick/',views.pick,name = "pick-clients"),
    path('active/',views.active,name = "active-clients"),
    path('update-profile-counsellor',views.updateProfileCounsellor,name="update-profile-counsellor")
]