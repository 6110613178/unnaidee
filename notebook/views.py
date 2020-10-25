from django.shortcuts import render
from .models import UserUn
from django.contrib.auth.models import User
def index(request):
    return render(request,'notebook/index.html')
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
        
        if password == confirmpassword:
            userun = UserUn.objects.create(
            firstname = name,
            lastname = surname,
            email = email,
            password = password,
            )
            user = User.objects.create_user(
            first_name = name,
            last_name = surname,
            email = email,
            password = password,
            )
            userun.save()
            user.save()
            return render(request,'notebook/login.html')
        else:
            return render(request,'notebook/register.html')
    return render(request,'notebook/register.html')