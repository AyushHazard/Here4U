from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Description
from .forms import *
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from counsellor.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from counsellor.models import *
# Create your views here.


def about(request):
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            return render(request,'counsellor/home2.html')
        else:
            return render(request,'client/about_us.html')
            
    return render(request,'client/about_us.html')


def home(request):
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        client = Clientdata.objects.all().filter(User=request.user)

        if client:
            return render(request,'client/home.html')
        else:
            return render(request,'counsellor/home2.html')
    else:
        return render(request,'client/home.html')
            
        

    

def profile(request):
    return render(request,'client/home.html')   


def signup(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect(updateProfile)
    else:
        form = UserCreationForm()

    return render(request,'client/signup.html',{'form':form})

# def login(request):
#     return render(request,'../registration/login.html')

# def logout(request):
#     return render(request,'../registration/logged_out.html')        

@login_required
def updateProfile(request):
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            return render(request,'counsellor/home2.html')
        
    form = UpdateProfileForm()
    context = {"form":form}
    if request.method=='POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            # user = Clientdata(**form.cleaned_data)
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            form = UpdateProfileForm()
            return render(request,'client/home.html')
        else:
            return render(request,'client/update-profile.html',context)
            
    return render(request,'client/update-profile.html',context)



def talk(request):
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            return render(request,'counsellor/home2.html')

    form = DescriptionForm()
    

    if request.method=='POST':
        form = DescriptionForm(request.POST,request.FILES)
        if form.is_valid():
            descrip =  Description(**form.cleaned_data)
            descrip.save()
            form = DescriptionForm()
            context = {"form":form,'all_counsellors': Counsellordata.objects.all(),"show":False,"message":"Saved successfully, Now please select a counsellor you would like to talk to."}
            # messages.success(request,'Your description has been saved successfully')
            return render(request,'client/talk_to_counsellor.html',context)
        else:
            context = {"form":form,"show":True,'all_counsellors': Counsellordata.objects.all()}
            return render(request,'client/talk_to_counsellor.html',context)
                
    else:
        context = {"form":form,"show":True,'all_counsellors': Counsellordata.objects.all()}
        return render(request,'client/talk_to_counsellor.html',context) 

    
    