from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect

def index(request):
	return HttpResponse("This is where you will enter a workout")
@csrf_protect
def signup(request):
	if request.method =="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password = raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm() 
	return render(request, 'workout/signup.html', {'form':form})

@csrf_protect
def login(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			username = request.REQUEST.get("username")
			password = request.REQUEST.get("password")

			user = user.authenticate(
				request, username=username, password=password)
			if user is not None:
				auth.login(request,user)
				return HttpResponse("Logged in")
			else:
				form=AuthenticationForm(request.POST)
				return HttpResponse("User not found")
	return render(request, 'workout/login.html', {'form':form})
