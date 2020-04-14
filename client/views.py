from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
	return render(request,'client/about_us.html')


def home(request):
	return render(request,'client/home.html')


def talk(request):
	return render(request,'client/talk_to_counsellor.html')	
	