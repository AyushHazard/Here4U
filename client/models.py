from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clientdata(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=32,choices=[('0','Male'),('1','Female'),('2','Others')])
    Age=models.IntegerField()
    Email=models.EmailField(primary_key=True)
    State=models.CharField(max_length=50,blank = True,null=True)
    City=models.CharField(max_length=50,blank = True,null=True)
    Marital_Status=models.CharField(max_length=32,choices=[('0','Single'),('1','Commited'),('2','Divorced'),('3','Married')])
    Educational_Status=models.CharField(max_length=32,choices=[('0','10th Pass'),('1','12th Pass'),('2','Graduate'),('3','Post-Graduate'),('4','Doctorate'),('5','Post-Doc')])
    
    def __str__(self):
        return self.Name

class Description(models.Model):
    # Email=models.ForeignKey(Clientdata,on_delete=models.CASCADE)
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    Message=models.CharField(max_length=1000) 
    extra_data=models.FileField(upload_to='client/uploads',null=True,blank=True)

    def __str__(self):
        return self.Message


class Counsellordata(models.Model):
    User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    Name=models.CharField(max_length=100)
    Gender=models.IntegerField(choices=[(0,'Male'),(1,'Female'),(2,'Other')])
    Age=models.IntegerField(blank = True,null=True)
    Profile_pic = models.FileField(blank=True,null=True)
    Email=models.EmailField()
    State=models.CharField(max_length=50,blank=True,null=True)
    City=models.CharField(max_length=50,blank=True,null=True)
    Education=models.CharField(max_length=300,blank = True,null=True)
    Expertise = models.CharField(max_length=200,blank=True,null=True)
    Summary = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.Name
