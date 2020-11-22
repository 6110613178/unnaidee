from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect


def layout(request):
    typeNotebook = ["Gaming", "Working & Light", "Toughness & Working"]
    sortNotebook = ["Newest", "Oldest", "Highest price", "Lowest price"]
    if request.user.is_authenticated:
        user1 = UserUn.objects.get(email = request.user.username)
        countfav = user1.favorite.all().count()
        return {
            "name" : user1,
            "log": "logout",
            "countfav": countfav,
            "typeNotebook": typeNotebook,
            "sortNotebook": sortNotebook
            }
    return{"log": "login", "typeNotebook": typeNotebook, "sortNotebook": sortNotebook}

def index(request):
    
    notebookall = NoteBook.objects.all()
    b = layout(request)
    if request.method == 'POST':
        f= request.POST["form"]
        if f == "search":
            input1 = request.POST['input1']
            input1 = input1.lower()
            notebookall = NoteBook.objects.all()
            notebooklist = []
            c = 0
            for notebook in notebookall:
                if notebook.search(input1):
                    notebooklist.append(notebook)
                    c = c+1
            b['notebookall']= notebooklist 
            if c==0:
                b['item'] = "Not found"
            elif c==1:
                b['item'] = "found "+str(c)+" item"
            else :
                b['item'] = "found "+str(c)+" items"      
            return render(request,'notebook/index.html',b)
        
        elif f == "filter":
            notebookFilter = request.POST['typeNotebook']
            notebookTypes = NoteBook.objects.filter(notebookdata__typeNotebook = notebookFilter)
            b['notebookall'] = notebookTypes
            return render(request,'notebook/index.html',b)

        elif f == "sort":
            notebookSort = request.POST['sortNotebook']
            if notebookSort == "Newest":
                notebookSorted = NoteBook.objects.all().order_by('-notebookdata__date')
                b['notebookall'] = notebookSorted
            if notebookSort == "Oldest":
                notebookSorted = NoteBook.objects.all().order_by('notebookdata__date')
                b['notebookall'] = notebookSorted
            elif notebookSort == "Highest price":
                notebookSorted = NoteBook.objects.all().order_by('-price')
                b['notebookall'] = notebookSorted
            elif notebookSort == "Lowest price":
                notebookSorted = NoteBook.objects.all().order_by('price')
                b['notebookall'] = notebookSorted
            return render(request, 'notebook/index.html',b)

    else :
        b['notebookall']= notebookall
        return render(request,'notebook/index.html',b)


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
        b = {}
        if name == '':
            b["errorname"]="Please assign Name"
        if surname == '':
            b["errorsurname"]="Please assign Surname"
        if email == '':
            b["erroremail"]="Please assign Email address"
        if password == '':
            b["errorpassword"]="Please assign Password"
        if (password == confirmpassword and password != '' and confirmpassword != '' and name != '' and surname != '' and email != ''): 
            if(UserUn.objects.filter(email = email).count() ==0):

                userun = UserUn.objects.create(firstname = name,lastname = surname,email = email,password = password,)
                user = User.objects.create_user(username = email,password = password)
                userun.save()
                user.save()
                return render(request,'notebook/login.html')
            else:
                return render(request,'notebook/register.html',{'message':"email are used"})
        else:
            b["message"]: "Confirm Password not correct"
    return render(request,'notebook/register.html')

def login_logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'notebook/login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "notebook/login.html", {
                "message": "Invalid credentials"
            })
    return render(request, "notebook/login.html")

def compare(request):
    notebookall = NoteBook.objects.all()
    compares = Compare.objects.all()
    b = layout(request)
    b['compares']= compares
    b['notebookall']= notebookall
    
    return render(request,'notebook/compare.html',b)

def calcompare(request):
    keynotebookobj = request.POST['notebook_id']
    noteobj = NoteBook.objects.get(id = keynotebookobj)
    cpustar = noteobj.cpu.star
    displaystar = noteobj.display.star
    gpustar = noteobj.gpu.star
    ramstar = noteobj.ram.star
    romstar = noteobj.rom.star
    allstar = (cpustar+gpustar+displaystar+ramstar+romstar)/5.0
    if (Compare.objects.filter(notebook = noteobj).count() == 0):
        saveobj = Compare.objects.create(notebook = noteobj,allstar = allstar)
        
    return redirect('compare')

def removecompare(request):
    keyobj = request.POST['rmcompare']
    obj = Compare.objects.get(notebook__id = keyobj)
    obj.delete()
    return redirect('compare')

def favorite(request):
    if not request.user.is_authenticated:
        return render(request, "notebook/login.html")
    else:
        user1 = UserUn.objects.get(email = request.user.username)
        notebookallfav = user1.favorite.all()
        b = layout(request)
        b['notebookallfav']= notebookallfav
        return render(request,'notebook/favorite.html',b)
    

def mark(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request, "notebook/login.html")
        else:
            idnotebook = request.POST["id"]
            user1 = UserUn.objects.get(email = request.user.username)
            notebook = NoteBook.objects.get(id = idnotebook )
            notebooks = user1.favorite.all()
            for x in notebooks:
                if x == notebook:
                    return HttpResponseRedirect(reverse('index'))
            user1.favorite.add(notebook)
            return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))

def unmarkfav(request):
    if request.method == "POST":
        idnotebook = request.POST["id"]
        user1 = UserUn.objects.get(email = request.user.username)
        notebook = NoteBook.objects.get(id = idnotebook)
        user1.favorite.remove(notebook)
        notebookallfav = user1.favorite.all()
        b = layout(request)
        b['notebookallfav']= notebookallfav
        return HttpResponseRedirect(reverse('favorite'),b)
    return HttpResponseRedirect(reverse('index'))

def notebook_page(request):
    if request.method == "POST":
        notebook_id = request.POST['notebook_id']
        notebook = NoteBook.objects.get(id = notebook_id)
        b = layout(request)
        b['notebook']= notebook
        return render(request,'notebook/notebookpage.html',b)
    return HttpResponseRedirect(reverse('index'))
