from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import re

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')
        
        if re.match(r'^\d', uname):
            return HttpResponse("Username cannot start with a number...!")
        

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already taken...!")
        
        if len(pass1)<5:
            return HttpResponse("Atleast 5 characters")

        if pass1 !=pass2:
            return HttpResponse("password didnt match...!")
        

        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or password incorrect...")
    return render(request, 'login.html')



def LogOut(request):
    logout(request)
    return redirect("login")