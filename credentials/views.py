from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('add')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
          if User.objects.filter(username=username).exists():
              messages.info(request,"Username Taken")
              return redirect('register')
          else:
             user=User.objects.create_user(username=username,password=password)
             user.save();
             return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def add(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        age= request.POST['age']
        gender = request.POST['gender']
        address=request.POST['address']
        phoneno= request.POST['phoneno']
        dob = request.POST['dob']
        district = request.POST['district']
        user=User.objects._create_user(username=username,email=email,age=age,gender=gender,address=address,phoneno=phoneno,dob=dob,district=district)
        user.save();
        return redirect('add')
    return render(request,"add.html")





