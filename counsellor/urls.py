from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "counsellor-home"),
    path('about/',views.about, name="counsellor-about"),
    path('pick/',views.pick,name = "pick-clients"),
    path('active/',views.active,name = "active-clients"),
]