from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from counsellor.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
# from counsellor.models import *
# Create your views here.


def about(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
        
            
    return render(request,'client/about_us.html',{"client":user_check})

def faqs(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
        
            
    return render(request,'client/faqs.html',{"client":user_check})


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




"""




    API VIEWS --- API VIEWS --- API VIEWS --- API VIEWS --- API VIEWS --- API VIEWS




"""
@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def GetUserId(request):
    user_id = request.user.id
    message = [{"id":user_id}]
    return Response(message)

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CreateClientProfileView(CreateAPIView):
    serializer_class = ClientdataSerializer
    permission_classes=[
    permissions.IsAuthenticated
    ]

@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def GetClientView(request,pk):
    # description = Description.objects.all()#.filter(pk=pk)
    user = User.objects.filter(id=pk).first()
    client = ClientdataSerializer(Clientdata.objects.filter(User=user),many=True)
    # for i in User.objects.all():
    #     print(i.username)
    return Response(client.data)

@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def GetCounsellorView(request,pk):
    # description = Description.objects.all()#.filter(pk=pk)
    user = User.objects.filter(id=pk).first()
    counsellor = CounsellordataSerializer(Counsellordata.objects.filter(User=user),many=True)
    # for i in User.objects.all():
    #     print(i.username)
    return Response(counsellor.data)        

class CreateCounsellorProfileView(CreateAPIView):
    serializer_class = CounsellordataSerializer
    permission_classes=[
    permissions.IsAuthenticated
    ]   

class UpdateCounserllorProfileView(UpdateAPIView):
    serializer_class = CounsellordataSerializer
    permissions_class=[
    permissions.IsAuthenticated
    ]
    lookup_field = 'User'
    queryset = Counsellordata.objects.all()   

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(User=self.request.user)
        return obj

class UpdateClientProfileView(UpdateAPIView):
    serializer_class = ClientdataSerializer
    permissions_class=[
    permissions.IsAuthenticated
    ]
    lookup_field = 'User'
    queryset = Clientdata.objects.all()   

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(User=self.request.user)
        print(obj)
        return obj        


class ListCounsellorsView(ListAPIView):
    queryset = Counsellordata.objects.all()
    serializer_class=CounsellordataSerializer
    permission_classes=[
    permissions.AllowAny
    ]

class CreateDescriptionView(CreateAPIView):
    serializer_class = DescriptionSerializer
    permission_classes=[
    permissions.IsAuthenticated
    ]

# ListDescriptionView : This view will fetch us the description of the user with primary key as pk

@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def GetDescriptionView(request,pk):
    # description = Description.objects.all()#.filter(pk=pk)
    user = User.objects.filter(id=pk).first()
    description = DescriptionSerializer(Description.objects.filter(User=user),many=True)
    # for i in User.objects.all():
    #     print(i.username)
    return Response(description.data)

@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def UserTypeCheck(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
    print(request.user)
    if user_check:
        message = [{"is_client": True,"status":"client"}]
    else:
        message = [{"is_client": False,"status":"counsellor"}]
                
    return Response(message)    

# To create a booking one needs to send in the user_id of client and counsellor and the time of booking
# One should also ensure in the front-end itself that the time entered by the user lies in the 
# appointment hours of the counsellor because this view directly creates an object without checking

class CreateBookingView(CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes=[
    permissions.IsAuthenticated
    ]
    

@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def GetActiveClientsView(request):
    obj = BookingSerializer(Bookings.objects.filter(counsellor_id=request.user.id),many=True)

    return Response(obj.data)

@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def GetActiveCounsellorsView(request):
    obj = BookingSerializer(Bookings.objects.filter(client_id=request.user.id),many=True)

    return Response(obj.data)    


@permission_classes([permissions.IsAuthenticated])
@api_view(('GET',))
def LogOutView(request):
    logout(request)
    return Response(None)


'''
NOTE  that the format for post should be like the example given below
                                                                        [
                                                                            {"username":"div"},
                                                                            {"password":"123"}
                                                                        ]
'''
@permission_classes([permissions.AllowAny])
class LogInView(APIView):
    def post(self, request, format=None):
        
        # print(request.POST['data '])

        # print(request.POST['data '])

        try:
            data = json.loads(request.POST['data '])    
        except:
            try:
                data = json.loads(request.POST['data'])
            except:    
                data = request.data    

        # data = request.data

        # print(request.POST['data '])
        print(data)

        try:
            # data = request.data
            username = data.get('username')
            password = data.get('password')
        except:
            # print("HEYYYYYYHEYYYYYYHEYYYYYYHEYYYYYYHEYYYYYYHEYYYYYYHEYYYYYY")
            data = request.POST['data ']
            
            username = data.get('username')
            password = data.get('password')


        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        print(user.is_authenticated)
        # login(request, user)

        # return Response(status=status.HTTP_200_OK)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

