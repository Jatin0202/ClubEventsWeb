from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'css_home.html')

