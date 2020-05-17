from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'css_login.html', {'error': 'Username or Password is incorrect.'})
    else:
        return render(request, 'css_login.html')

def signUP(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'signup.html',{'error':'Username has already been taken'})
        #User has info and wants an account
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})

    else:
        #User wants to enter info
        return render(request, 'signup.html')


def logout2(request):
    # if request.method == 'POST':
    logout(request)
    return redirect('home')