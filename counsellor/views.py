from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
	return render(request,'counsellor/about_us2.html')


def home(request):
	return render(request,'counsellor/home2.html')


def pick(request):
	return render(request,'counsellor/pick_clients.html')

def active(request):
	return render(request,'counsellor/active_clients.html')		
	