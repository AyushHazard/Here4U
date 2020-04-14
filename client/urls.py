from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "client-home"),
    path('about/',views.about, name="client-about"),
    path('talk/',views.talk,name = "talk-to-counsellor"),

]