
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.models import User, auth
from social.models import campaign

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def upload(request):
    return render(request, "upload.html")

def post_success(request):
    title= request.POST["title"]
    des= request.POST["des"]
    img= request.FILES["img"]
    camp2 = campaign(title=title, des=des, img=img, )

    camp2.save()
    return redirect('/')

def profile(request):
    return render(request, "profile.html")

def option(request):
    return render(request, "two.html")

def business(request):
    return render(request, "business.html")

def post_success2(request):
    title= request.POST["title"]
    des= request.POST["des"]
    com= request.POST["com"]
    lin= request.POST["lin"]
    img= request.FILES["img"]
    camp3 = campaign(title=title, des=des, img=img, com=com, lin=lin)

    camp3.save()
    return redirect('/')


