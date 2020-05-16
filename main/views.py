from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  login,logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from .forms import NewUserForm,DataSubmitForm
from .models import Chart,DataProcess,Post,MessageUs
from django.contrib.auth.decorators import login_required
from . import forms



# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name="main/header.html",
				  context={"market": Chart.objects.all})

	

def sendData(request):
		if request.method == 'POST':
			if request.POST.get('email') and request.POST.get('file') and request.POST.get('message') :
				data=DataProcess()
				data.email= request.POST.get('email')
				data.file= request.POST.get('file')
				data.body= request.POST.get('message')
				data.author = request.user
				data.save()
				messages.info(request, "Your Data has Been Sent")
				return render(request,'main/header.html')
 

		else:
			   return redirect('main:homepage')			
 


def createpost(request):
		if request.method == 'POST':
			if request.POST.get('title') and request.POST.get('content'):
				post=Post()
				post.title= request.POST.get('title')
				post.content= request.POST.get('content')
				post.save()
				
				return render(request,'main/header.html')
 

		else:
			   return redirect('main:homepage')

def zender(request):
		if request.method == 'POST':
			if request.POST.get('email1') and request.POST.get('yMessage') and request.POST.get('date'):
				post=MessageUs()
				post.email1= request.POST.get('email1')
				post.yMessage= request.POST.get('yMessage')
				post.date= request.POST.get('date')
				post.save()
				# sending email to user
				zEmail = request.POST.get('email1')
				subject='Data-Farm'
				Emessage='Thank you for sending us a message,  We will be with you shortly'
				from_email=settings.EMAIL_HOST_USER
				to_list=[zEmail]
				send_mail(
				     subject,
				     Emessage,
				     from_email,
				     to_list,
				    fail_silently=False,
				)
				messages.info(request, "Message has been Sent...Kindly wait for response")
				messages.info(request, f"An Email has been Sent to {zEmail}")
				return render(request,'main/header.html')
 

		else:
			   return redirect('main:homepage')

def register(request):
	if request.method == "POST":
		form =NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			# sending email to user
			sEmail = form.cleaned_data.get('email1')
			subject='Appreciation From Data-Farm'
			Emessage='Thank you for singning up onto Data-Farm, we are here to./n We promise to give you the best of our services '
			from_email=settings.EMAIL_HOST_USER
			to_list=[user.email]
			send_mail(
			     subject,
			     Emessage,
			     from_email,
			     to_list,
			    fail_silently=False,
			)
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			messages.info(request, f"An email has been sent to  {sEmail}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
 

	form = NewUserForm
	return render(request,
				  "main/register.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})
