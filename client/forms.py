from django import forms
from .models import *

class DescriptionForm(forms.Form):
    Message=forms.CharField(label = "Message", max_length=1000,help_text="Write your heart out !!!") 
    extra_data=forms.FileField(label = "extra_data")
    

