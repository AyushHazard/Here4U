from django import forms
from django.forms import ModelForm
from .models import *

# class DescriptionForm(forms.Form):
#     Message=forms.CharField(label = "Message", max_length=1000,help_text="Write your heart out !!!") 
#     extra_data=forms.FileField(label = "extra_data",required=False)

# class UpdateProfileForm(forms.Form):
#     Name=forms.CharField(label = "Name *",max_length=100,help_text="Set an alias if you do not wish to disclose your name")
#     Gender=forms.ChoiceField(label = "Gender *",choices=(('','Gender'),('0','Male'),('1','Female'),('2','Others')))
#     Age=forms.IntegerField(label = "Age *")
#     Email=forms.EmailField(label = "Email *",help_text="Will remain confidential")
#     State=forms.CharField(label = "State",max_length=50,required=False)
#     City=forms.CharField(label = "City",max_length=50,required=False)
#     Marital_Status=forms.ChoiceField(label = "Marital Status *",choices=(('','Marital Status'),('0','Single'),('1','Commited'),('2','Divorced'),('3','Married')))
#     Educational_Status=forms.ChoiceField(label = "Educational Status *",choices=(('','Educational Status'),('0','10th Pass'),('1','12th Pass'),('2','Graduate'),('3','Post-Graduate'),('4','Doctorate'),('5','Post-Doc')))

class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = ['Message','extra_data']

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Clientdata
        fields = ['Name','Gender','Age','Email','State','City','Marital_Status','Educational_Status']


class UpdateProfileFormCounsellor(ModelForm):
    class Meta:
    	model = Counsellordata
    	fields = ['Name','Gender','Age','Profile_pic','Email','State','City','Education','Expertise','Summary']        
