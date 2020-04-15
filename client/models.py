from django.db import models

# Create your models here.
class Userdata(models.Model):
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=32,choices=[(0,'Male'),(1,'Female'),(2,'Other')])
    Age=models.IntegerField()
    Email=models.EmailField()
    State=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    Marital_Status=models.CharField(max_length=32,choices=[(0,'Single'),(1,'Commited'),(2,'Divorced'),(3,'Married')])
    Educational_Status=models.CharField(max_length=32,choices=[(0,'10th'),(1,'12th'),(2,'Graduate'),(3,'Post-Graduate'),(4,'Doctorate'),(5,'Post-Doc')]) 