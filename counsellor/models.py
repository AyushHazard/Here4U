from django.db import models
# Create your models here.
class Counsellordata(models.Model):
    Name=models.CharField(max_length=100)
    Gender=models.IntegerField(max_length=32,choices=[(0,'Male'),(1,'Female'),(2,'Other')])
    Age=models.IntegerField()
    # Profile_pic = models.FileField()
    Email=models.EmailField()
    State=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    Educational_Status=models.CharField(max_length=32,choices=[('a','10th'),('b','12th'),('c','Graduate'),('d','Post-Graduate'),('e','Doctorate'),('f','Post-Doc')])

    def __str__(self):
        return self.Name


