from django.shortcuts import render
from .models import UserUn
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    if request.user.is_authenticated:
        user1 = UserUn.objects.get(email= request.user.username)
        return render(request,'notebook/index.html',{"name" : user1,"log": "logout"})
    return render(request,'notebook/index.html',{"log": "login"})
def about(request):
    return render(request,'notebook/about.html')
def register(request):
    return render(request,'notebook/register.html')

def addregister(request):
    if request.method == 'POST':
        name = request.POST['firstname']
        surname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password1 == confirmpassword1:
            userun = UserUn.objects.create(
            firstname = name,
            lastname = surname,
            email = email,
            password = password,
            )
            user = User.objects.create_user(
            username = email,
            password = password
            )
            userun.save()
            user.save()
            return render(request,'notebook/login.html')
        else:
            return render(request,'notebook/register.html')
    return render(request,'notebook/register.html')
def login_logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'notebook/login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "notebook/login.html", {
                "message": "Invalid credentials"
            })
    return render(request, "notebook/login.html")


    