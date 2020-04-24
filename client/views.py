from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from counsellor.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# from counsellor.models import *
# Create your views here.


def about(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
        
            
    return render(request,'client/about_us.html',{"client":user_check})


def home(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    return render(request,'client/home.html',{"client":user_check})
            
        

    

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

    return render(request,'client/signup.html',{'form':form,"client":False})

# def login(request):
#     return render(request,'../registration/login.html')

# def logout(request):
#     return render(request,'../registration/logged_out.html')        

@login_required
def updateProfile(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
        
    form = UpdateProfileForm()
    context = {"form":form,"client":user_check}
    if request.method=='POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            # user = Clientdata(**form.cleaned_data)
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            form = UpdateProfileForm()
            return render(request,'client/home.html',{"client":user_check})
        else:
            return render(request,'client/update-profile.html',context)
            
    return render(request,'client/update-profile.html',context)

# Talk to a counsellor View

def talk(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
            return render(request,'client/home.html',{"client":user_check})

    form = DescriptionForm()
    show = True
    if request.user.is_authenticated:
        des = Description.objects.all().filter(User=request.user)
        if des:
            show = False
    

    if request.method=='POST':
        # @login_required
        form = DescriptionForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            form = DescriptionForm()
            context = {"form":form,"client":True,'all_counsellors': Counsellordata.objects.all(),"show":False,"message":"Saved successfully, Now please select a counsellor you would like to talk to."}
            # messages.success(request,'Your description has been saved successfully')
            return render(request,'client/talk_to_counsellor.html',context)
        else:
            context = {"form":form,"client":True,"show":show,'all_counsellors': Counsellordata.objects.all()}
            return render(request,'client/talk_to_counsellor.html',context)
                
    else:
        context = {"form":form,"client":True,"show":show,'all_counsellors': Counsellordata.objects.all()}
        return render(request,'client/talk_to_counsellor.html',context) 


## Booking View 

@login_required
def book(request,pk):
    counsellor = Counsellordata.objects.get(pk=pk)
    if not counsellor:
        return redirect(talk)

    form = BookingForm()
    check = ActiveCounsellor.objects.filter(user = request.user, Counsellor=counsellor.User)

    if not check:
        context={"form":form,"client":True,"counsellor":counsellor}
        if request.method=='POST':
            form = BookingForm(request.POST)
            instance = form.save(commit=False)
            if form.is_valid() and instance.Booking_time>=counsellor.Consultation_start and instance.Booking_time<= counsellor.Consultation_end:
                
                instance.user = request.user
                instance.Counsellor = counsellor.User
                active_client = ActiveClient(user=counsellor.User,Client=request.user,Booking_time=instance.Booking_time)
                instance.save()
                active_client.save()
                return redirect(sessions)
            else:
                form = BookingForm()
                return render(request,'client/book.html',context)
                

        else:
            return render(request,'client/book.html',context)

    return redirect(talk)


## Active Sessions view

@login_required
def sessions(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
            return render(request,'client/home.html',{"client":user_check})
    all_counsellors = []
    time = []
    for obj in ActiveCounsellor.objects.all().filter(user=request.user):
        counsellor = obj.Counsellor
        time.append(obj.Booking_time)
        # print(counsellor)
        all_counsellors.append(Counsellordata.objects.get(User=counsellor))

    content = {"client":user_check,"all_counsellors":zip(all_counsellors,time)}
    return render(request,'client/active_sessions.html',content)


# Counsellor Views



def pick(request):
    user_check = False
    if request.user.is_authenticated:
        client = Clientdata.objects.all().filter(User=request.user)
        if client:
            user_check = True
            return render(request,'client/home.html',{"client":user_check})

    return render(request,'client/pick_clients.html',{"client":user_check})

def active(request):
    user_check = False
    if request.user.is_authenticated:
        client = Clientdata.objects.all().filter(User=request.user)
        if client:
            user_check = True
            return render(request,'client/home.html',{"client":user_check})

    all_clients = []
    time = []
    for obj in ActiveClient.objects.all().filter(user=request.user):
        client = obj.Client
        time.append(obj.Booking_time)
        # print(counsellor)
        all_clients.append(Clientdata.objects.get(User=client))        

    return render(request,'client/active_clients.html',{"client":user_check,"all_clients":zip(all_clients,time)})    


def updateProfileCounsellor(request):
    user_check = False
    if request.user.is_authenticated:
        client = Clientdata.objects.all().filter(User=request.user)
        if client:
            user_check = True
            return render(request,'client/home.html',{"client":user_check})

    form = UpdateProfileFormCounsellor
    context = {"form":form,"client":user_check}
    if request.method=='POST':
        form = UpdateProfileFormCounsellor(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            form = UpdateProfileFormCounsellor()
            return render(request,'client/home.html',{"client":user_check})
        else:
            return render(request,'client/update-profile-counsellor.html',context)
            
    return render(request,'client/update-profile-counsellor.html',context)    
    