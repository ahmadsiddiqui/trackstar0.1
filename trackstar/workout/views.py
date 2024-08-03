from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect

def index(request):
	return render(request, 'workout/index.html')

def home_screen_view(request):
	context = {}

	return render(request,"workout/home.html",context)