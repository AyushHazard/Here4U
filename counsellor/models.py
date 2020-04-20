from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Counsellordata(models.Model):
#     User = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
#     Name=models.CharField(max_length=100)
#     Gender=models.IntegerField(max_length=32,choices=[(0,'Male'),(1,'Female'),(2,'Other')])
#     Age=models.IntegerField(blank = True,null=True)
#     Profile_pic = models.FileField(blank=True,null=True)
#     Email=models.EmailField()
#     State=models.CharField(max_length=50,blank=True,null=True)
#     City=models.CharField(max_length=50,blank=True,null=True)
#     Education=models.CharField(max_length=300,blank = True,null=True)
#     Expertise = models.CharField(max_length=200,blank=True,null=True)
#     Summary = models.CharField(max_length=1000,blank=True,null=True)

#     def __str__(self):
#         return self.Name


