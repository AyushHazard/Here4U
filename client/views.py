from django.shortcuts import render
from django.http import HttpResponse
from .models import Description
from .forms import DescriptionForm
from django.views.generic import CreateView
from django.contrib import messages
from counsellor.models import *
# Create your views here.


def about(request):
	return render(request,'client/about_us.html')


def home(request):
	return render(request,'client/home.html')




def talk(request):
	form = DescriptionForm()
	
	  

	

	if request.method=='POST':
		form = DescriptionForm(request.POST,request.FILES)
		if form.is_valid():
			descrip =  Description(**form.cleaned_data)
			descrip.save()
			form = DescriptionForm()
			context = {"form":form,'all_counsellors': Counsellordata.objects.all(),"show":False,"message":"Saved successfully, Now please select a counsellor you would like to talk to."}
			# messages.success(request,'Your description has been saved successfully')
			return render(request,'client/talk_to_counsellor.html',context)
		else:
			context = {"form":form,"show":True,'all_counsellors': Counsellordata.objects.all()}
			return render(request,'client/talk_to_counsellor.html',context)
				
	else:
		context = {"form":form,"show":True,'all_counsellors': Counsellordata.objects.all()}
		return render(request,'client/talk_to_counsellor.html',context)	

	
	