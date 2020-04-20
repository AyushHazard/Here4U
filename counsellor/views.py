from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from client.models import *
# Create your views here.


# def about(request):
#     if request.user.is_authenticated:
#         client = Clientdata.objects.all().filter(User=request.user)
#         if client:
#             return render(request,'client/home.html')
#     return render(request,'counsellor/about_us2.html')


# def home(request):
#     if request.user.is_authenticated:
#         client = Clientdata.objects.all().filter(User=request.user)
#         if client:
#             return render(request,'client/home.html')
#     return render(request,'counsellor/home2.html')


# def pick(request):
#     if request.user.is_authenticated:
#         client = Clientdata.objects.all().filter(User=request.user)
#         if client:
#             return render(request,'client/home.html')
#     return render(request,'counsellor/pick_clients.html')

# def active(request):
#     if request.user.is_authenticated:
#         client = Clientdata.objects.all().filter(User=request.user)
#         if client:
#             return render(request,'client/home.html')
#     return render(request,'counsellor/active_clients.html')     

# def updateProfile(request):
#     if request.user.is_authenticated:
#         client = Clientdata.objects.all().filter(User=request.user)
#         if client:
#             return render(request,'client/home.html')
#     form = UpdateProfileForm
#     context = {"form":form}
#     if request.method=='POST':
#         form = UpdateProfileForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.User = request.user
#             instance.save()
#             form = UpdateProfileForm()
#             return render(request,'counsellor/home2.html')
#         else:
#             return render(request,'counsellor/update-profile-counsellor.html',context)
            
#     return render(request,'counsellor/update-profile-counsellor.html',context)
#     