from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def signup_view(request):
    if request.method=='GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        username=request.POST.get('username')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if not username or not pass1 or not pass2:
            return render(request,'signup.html',{'form':UserCreationForm,'error':"All fields are required"})
        if pass1==pass2:
            try:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                login(request,user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm,'error':"Username already exists"})
        else:
            return render(request,'signup.html',{'form':UserCreationForm,'error':"Passwords do not match"})
def login_view(request):
    if request.method=='GET':
        return render(request,'login.html',{'form':AuthenticationForm})
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            return render(request,'login.html',{'form':AuthenticationForm,'error':"Username and password do not match"})
        else:
            login(request,user)
            return redirect('dashboard')
@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')
@login_required
def dashboard_view(request):
    return render(request,'dashboard.html',{'user':request.user})