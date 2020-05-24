from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# CLIENT MODELS

class Clientdata(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    # user_id = models.IntegerField(null = True,blank = True)
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=32,choices=[('Male','Male'),('Female','Female'),('Others','Others')])
    Age=models.IntegerField()
    Email=models.EmailField(primary_key=True)
    State=models.CharField(max_length=50,blank = True,null=True)
    City=models.CharField(max_length=50,blank = True,null=True)
    Marital_Status=models.CharField(max_length=32,choices=[('Single','Single'),('Commited','Commited'),('Divorced','Divorced'),('Married','Married')])
    Educational_Status=models.CharField(max_length=32,choices=[('10th Pass','10th Pass'),('12th Pass','12th Pass'),('Graduate','Graduate'),('Post_Graduate','Post_Graduate'),('Doctorate','Doctorate'),('Post_Doc','Post_Doc')])
    
    def __str__(self):
        return self.Name

class Description(models.Model):
    # Email=models.ForeignKey(Clientdata,on_delete=models.CASCADE)
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    Message=models.CharField(max_length=1000) 
    extra_data=models.FileField(upload_to='client/uploads',null=True,blank=True)

    def __str__(self):
        return self.Message

class VideoCallLink(models.Model):
    counsellor =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    client =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='cl_video')
    link = models.TextField()

    def __str__(self):
        return self.link

class ActiveCounsellor(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='client_id_clside')
    Counsellor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='counsellor_id_clside')
    Booking_time = models.TimeField(null=True,auto_now=False, auto_now_add=False)


class Bookings(models.Model):
    client = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='client_user')
    client_key = models.IntegerField(blank = True,null=True)
    counsellor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='counsellor_user')
    counsellor_key = models.IntegerField(blank=True,null = True)
    Booking_time = models.TimeField(null=True,auto_now=False, auto_now_add=False)
# COUNSELLOR MODELS

class Counsellordata(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    # user_id = models.IntegerField(null = True,blank = True)
    Name = models.CharField(max_length=100)
    Gender=models.IntegerField(choices=[(0,'Male'),(1,'Female'),(2,'Other')])
    Age=models.IntegerField(blank = True,null=True)
    Profile_pic = models.FileField(blank=True,null=True)
    Email=models.EmailField()
    State=models.CharField(max_length=50,blank=True,null=True)
    City=models.CharField(max_length=50,blank=True,null=True)
    Education=models.CharField(max_length=300,blank = True,null=True)
    Expertise = models.CharField(max_length=200,blank=True,null=True)
    Summary = models.CharField(max_length=1000,blank=True,null=True)
    Consultation_start = models.TimeField(null=True,auto_now=False, auto_now_add=False)
    Consultation_end = models.TimeField(null=True,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.Name

class ActiveClient(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='counsellor_id_coun')
    Client = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='client_id_coun')
    Booking_time = models.TimeField(null=True,auto_now=False, auto_now_add=False)

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='sender')   
    reciever = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='reciever')
    body = models.TextField()
    time = models.TimeField(null = True,auto_now = True,auto_now_add = False)

    def __str__(self):
        return self.body

class ActiveMessages(models.Model):
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='active_sender')   
    reciever = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='active_reciever')            

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,null = True)
    body = models.TextField()
    brief = models.TextField(null = True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        print(self.id)
        return reverse('blog')



