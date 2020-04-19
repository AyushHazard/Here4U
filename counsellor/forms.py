from django import forms
from django.forms import ModelForm
from .models import *

class UpdateProfileForm(ModelForm):
    class Meta:
    	model = Counsellordata
    	fields = ['Name','Gender','Age','Profile_pic','Email','State','City','Education','Expertise','Summary']