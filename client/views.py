from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json
from django.views.generic import CreateView,ListView, DetailView
from .models import Post
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
from django.contrib.auth.mixins import LoginRequiredMixin
# from counsellor.models import *
# Create your views here.

#def blog(request):
#    return render(request,'client/blog.html',{'posts': Post.objects.all()})





@login_required
def createPostView(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    if request.method=='POST':
        brief = request.POST['body'][:200]+"..."

        if request.POST['body']!='':
            new_post = Post.objects.create(title = request.POST['title'],author=request.user,body=request.POST['body'],brief=brief)        

        return redirect(blogListView)
        
    return render(request,'client/blog_post.html',{"client":user_check})        



def blogListView(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    posts = Post.objects.all()

    all_posts = []

    for i in posts:
        all_posts.append(i)

    all_posts.sort(key = lambda x: x.time, reverse = True) 

    # print(all_posts)

    # We'll sort by date-time

    return render(request,'client/blog.html',{"all_posts":all_posts,"client":user_check})   

@login_required
def personalBlogListView(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False


    all_posts = Post.objects.filter(author=request.user)

    # We'll sort by date-time

    return render(request,'client/blogs-personal.html',{"all_posts":all_posts,"client":user_check}) 

@login_required
def deleteBlog(request,pk):
    


    post = Post.objects.get(pk=pk)

    if request.user==post.author:
        post.delete()

    return redirect(personalBlogListView) 

@login_required
def updateBlogView(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False


    post = Post.objects.get(pk=pk)

    if request.user!=post.author:
        
        return redirect(blogListView) 

    if request.method=='POST':
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.brief = request.POST['body'][:200] + '...'
        post.save()
        return redirect(personalBlogListView)


    return render(request,'client/blog-update.html',{"post":post})    
               

def blogDetailView(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    blog = Post.objects.get(pk=pk)        


    return render(request,'client/blog_detail.html',{"client":user_check,"post":blog})     

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

@login_required
def myProfile(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False 

    
    userDescription = Description.objects.filter(User=request.user)
    profData = None

    if user_check:
        profData = Clientdata.objects.get(User=request.user)  
    else:
        profData = Counsellordata.objects.get(User=request.user)    

    if userDescription:
        userDescription = userDescription[0]   


    if user_check:
        return render(request,'client/my-profile-client.html',{"client":user_check,"description":userDescription,"profData":profData})   
    else:
        return render(request,'client/my-profile-counsellor.html',{"client":user_check,"profData":profData}) 

def counsellorProfile(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False 

    
    # userDescription = Description.objects.filter(User=request.user)
    profData = Counsellordata.objects.get(pk=pk) 

      
    return render(request,'client/counsellor-profile.html',{"client":user_check,"profData":profData})
                    


@login_required
def clientDescription(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    Client = User.objects.get(id=pk) 
    ClientObj = None      
    userDescription = None    
    findBooking = ActiveBookings.objects.filter(client=Client,counsellor=request.user)

    # We need to ensure that only the counsellor that the user has booked can view the description and not one else even by
    # Editing the urls

    if user_check==False and findBooking:
        userDescription = Description.objects.filter(User=Client)
        ClientObj = Clientdata.objects.get(User=Client) 

    if Client==request.user:
        userDescription = Description.objects.filter(User=Client)   # If the user himself wants to see the description
        ClientObj = Clientdata.objects.get(User=Client) 


        
    if userDescription:
        userDescription = userDescription[0]

    # print(userDescription.extra_data)    

    
    return render(request,'client/view-description.html',{"client":user_check,"description":userDescription,"profData":ClientObj})    

@login_required
def sessNotes(request,pk):

    Client = User.objects.get(id=pk)


    if request.method=='POST':
        sess_notes = sessionNotes(client=Client,counsellor=request.user,title=request.POST["title"],about=request.POST["about"])
        # if request.POST.find('notesFile'):
        #     sess_notes.file = request.POST['notesFile']
        sess_notes.save()

    
    old_notes_query = sessionNotes.objects.filter(client = Client, counsellor = request.user)

    old_notes = []

    ###   Might be inefficient   CONSIDER CHANGING IF WEBSITE IS SLOW

    for i in old_notes_query:
        old_notes.append(i)

    
    old_notes.sort(key = lambda x: x.time, reverse = True) 


    return render(request,'client/session-notes.html',{"old_notes":old_notes,"name":Client.first_name}) 

@login_required
def viewSessNotes(request,pk):

    note = sessionNotes.objects.get(pk=pk)

    actualCoun = note.counsellor

    if not actualCoun==request.user:
        note = None

    if note:    
        return render(request,'client/session-notes-view.html',{"note":note}) 
    else:
        return redirect(home)       

@login_required
def delSessNotes(request,pk):

    note = sessionNotes.objects.get(pk=pk)

    actualCoun = note.counsellor

    if actualCoun==request.user:
        cl = note.client
        note.delete()
        return redirect(sessNotes,pk=cl.id)
    else:
        return redirect(home)
        


@login_required
def videoCall(request):

    return render(request,'client/video-call.html')

@login_required
def interfaceClient(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    Client = User.objects.get(id=pk)
    name = Client.first_name
    # present = False

    try:    
        curr_links = VideoCallLink.objects.get(counsellor=request.user)
        # present = True
    except:
        curr_links = None   

    # print("HEYA")     


    if request.method=='POST':
        VideoCallLink.objects.filter(counsellor=request.user).delete()
        video_link = VideoCallLink.objects.create(counsellor = request.user,client = Client, link = request.POST["videocall-link"])

        return redirect(interfaceClient,pk=pk)


    return render(request,'client/connect-client.html',{"links":curr_links,"client":user_check,"name":name})

@login_required
def interfaceCounsellor(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    Counsellor = User.objects.get(id=pk)
    # present = False

    try:
        curr_links = VideoCallLink.objects.get(counsellor=Counsellor,client = request.user)
        # present = True
    except:
        curr_links = None
         

    return render(request,'client/connect-counsellor.html',{"links":curr_links,"client":user_check})      
            
def deleteLink(request,pk):

    
    link = VideoCallLink.objects.filter(pk=pk)

    if link:
        ppk = link[0].client.id
    else:
        ppk = None    

    link.delete()    

    return redirect(interfaceClient,pk=ppk)

@login_required
def messages(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    ###   Might be inefficient   CONSIDER CHANGING IF WEBSITE IS SLOW        

    all_messages = []
    for i in ActiveMessages.objects.filter(sender = request.user):
        all_messages.append(i)
    
    for i in ActiveMessages.objects.filter(reciever = request.user):
        all_messages.append(i) 

    other = []
    Current = request.user

    for i in all_messages:
        if i.sender == Current:
            other.append(i.reciever)
        else:
            other.append(i.sender)    

    
    return render(request,'client/messages.html',{"client":user_check,"messages":other})    

@login_required
def messageDetail(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
    # pk will contain the reciever's id
    # reciever = User.objects.get(id=pk)

    Sender = request.user
    Reciever = User.objects.get(id=pk)

    conversation = []

    for i in Message.objects.filter(sender = Sender, reciever = Reciever):
        conversation.append(i)

    for i in Message.objects.filter(sender = Reciever, reciever = Sender):
        conversation.append(i)

    conversation.sort(key = lambda x: x.time, reverse = False)    

    # for i in conversation:
    #     print(i.time)
    

    # print(Sender)
    # print(Reciever)

    if request.method=='POST':
        # print(request.POST["message-body"])
        found = ActiveMessages.objects.filter(sender = Sender, reciever = Reciever)
        dus = ActiveMessages.objects.filter(reciever = Sender, sender = Reciever)
        if not found and not dus:
            # print("NOT FOUND")
            if request.POST["message-body"]!='':
                ActiveMessages.objects.create(sender = Sender, reciever = Reciever)

        if request.POST["message-body"]!='':
            new_message = Message.objects.create(sender = Sender,reciever = Reciever, body = request.POST["message-body"])
        # print(new_message.time)
        return redirect(messageDetail,pk=pk)


    return render(request,'client/message-detail.html',{"client":user_check,"convo":conversation})


    

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
            curr = request.user
            curr.first_name = request.POST["Name"]
            curr.save()
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            form = UpdateProfileForm()
            return render(request,'client/home.html',{"client":user_check})
        else:
            return render(request,'client/update-profile.html',context)
            
    return render(request,'client/update-profile.html',context)

@login_required
def editProfileClient(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
            return redirect(home)

    obj = Clientdata.objects.get(User = request.user)

    form = UpdateProfileForm({'Name':obj.Name,'Gender':obj.Gender,'Age':obj.Age,'Email':obj.Email,'State':obj.State,'City':obj.City,'Marital_Status':obj.Marital_Status,'Educational_Status':obj.Educational_Status}) 

    context = {"form":form,"client":user_check}

    if request.method=='POST':
        obj.Name = request.POST['Name']
        obj.Gender = request.POST['Gender']
        obj.Age = request.POST['Age']
        obj.Email = request.POST['Email']
        obj.State = request.POST['State']
        obj.City = request.POST['City']
        obj.Marital_Status = request.POST['Marital_Status']
        obj.Educational_Status = request.POST['Educational_Status']

        obj.save()

        return redirect(myProfile)


    return render(request,'client/edit-profile-client.html',context)

    
@login_required
def editProfileCounsellor(request):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
            

    if user_check:
        return redirect(home)

    obj = Counsellordata.objects.get(User = request.user)

    form = UpdateProfileFormCounsellor({'Name':obj.Name,'Gender':obj.Gender,'Age':obj.Age,'Email':obj.Email,'State':obj.State,'City':obj.City,'Education':obj.Education,'Expertise':obj.Expertise,'Summary':obj.Summary,'Consultation_start':obj.Consultation_start,'Consultation_end':obj.Consultation_end}) 

    context = {"form":form,"client":user_check}

    if request.method=='POST':
        obj.Name = request.POST['Name']
        obj.Gender = request.POST['Gender']
        obj.Age = request.POST['Age']
        obj.Email = request.POST['Email']
        obj.State = request.POST['State']
        obj.City = request.POST['City']
        obj.Education = request.POST['Education']
        obj.Expertise = request.POST['Expertise']
        obj.Summary = request.POST['Summary']
        obj.Consultation_start = request.POST['Consultation_start']
        obj.Consultation_end = request.POST['Consultation_end']

        obj.save()

        return redirect(myProfile)


    return render(request,'client/edit-profile-counsellor.html',context)    

@login_required
def deleteDescription(request,pk):

    obj = Description.objects.get(pk=pk)

    if(obj.User==request.user):
        obj.delete()

    return redirect(myProfile) 
@login_required
def deleteBooking(request,pk):

    obj = ActiveBookings.objects.get(client=request.user,counsellor_id=pk)

    if(obj.client==request.user):
        obj.delete()

    return redirect(sessions)        

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
    
    summaries = []

    for i in Counsellordata.objects.all():
        if i.Summary:
            summaries.append(i.Summary[:200] + "...")
        else:
            summaries.append("")    

    all_counsellors = Counsellordata.objects.all()    

    if request.method=='POST':
        # @login_required
        form = DescriptionForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            form = DescriptionForm()
            context = {"form":form,"client":True,'all_counsellors': zip(all_counsellors,summaries),"show":False,"message":"Saved successfully, Now please select a counsellor you would like to talk to."}
            # messages.success(request,'Your description has been saved successfully')
            return render(request,'client/talk_to_counsellor.html',context)
        else:
            context = {"form":form,"client":True,"show":show,'all_counsellors': zip(all_counsellors,summaries)}
            return render(request,'client/talk_to_counsellor.html',context)
                
    else:
        context = {"form":form,"client":True,"show":show,'all_counsellors': zip(all_counsellors,summaries)}
        return render(request,'client/talk_to_counsellor.html',context) 


## Booking View 

@login_required
def book(request,pk):
    user_check = True
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False

    counsellor = Counsellordata.objects.get(pk=pk)
    if not counsellor or not user_check:
        return redirect(talk)

    form = BookingForm()
    check = ActiveBookings.objects.filter(client = request.user, counsellor=counsellor.User)

    if not check:
        context={"form":form,"client":user_check,"counsellor":counsellor}
        if request.method=='POST':
            form = BookingForm(request.POST)
            instance = form.save(commit=False)
            if form.is_valid() and instance.Booking_time>=counsellor.Consultation_start and instance.Booking_time<= counsellor.Consultation_end:
                
                instance.client = request.user
                instance.counsellor = counsellor.User
                # active_client = ActiveClient(user=counsellor.User,Client=request.user,Booking_time=instance.Booking_time)
                instance.save()
                # active_client.save()
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
    for obj in ActiveBookings.objects.filter(client=request.user):
        counsellor = obj.counsellor
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
    for obj in ActiveBookings.objects.filter(counsellor=request.user):
        client = obj.client
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
            curr = request.user
            curr.first_name = request.POST["Name"]
            curr.save()
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
    message = {"id":user_id}
    return Response(message)

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    
    serializer = UserSerializer(request.user)
    print(serializer.data)
    return Response(serializer.data)    

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializerWithToken
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

@permission_classes([permissions.AllowAny])
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
    serializer_class=CounsellordataGETSerializer
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
    print(1)
    if request.user.is_authenticated:
        coun = Counsellordata.objects.all().filter(User=request.user)
        if coun:
            user_check = False
    print(request.user)
    if user_check:
        message = {"status":"client"}
    else:
        message = {"status":"counsellor"}
                
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

