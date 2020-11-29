from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from main import uploadFile

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
            "sortNotebook": sortNotebook,
            "profile" : "profile"
            }
    return{"log": "login","register":"register" ,"typeNotebook": typeNotebook, "sortNotebook": sortNotebook}

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
    return render(request,'notebook/register.html',b)

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
            if request.user.is_superuser == 1:
                return HttpResponseRedirect(reverse('showadmin'))
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

def profile(request):
    user = UserUn.objects.get(email = request.user.username)    
    b = {"user" : user}
    return render(request,'notebook/profile.html', b)

def editprofile(request):
    user = UserUn.objects.get(email = request.user.username)     
    b = {}
    b['user'] = user
    b['firstname']=user.firstname
    b['lastname']=user.lastname
    b['email']=user.email
    return render(request,'notebook/editprofile.html', b)

def editprofilevalue(request):
    email = request.user.username

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    password = request.POST['password']
    newpassword = request.POST['newpassword']
    confirmnewpassword = request.POST['confirmnewpassword']
    obj = UserUn.objects.get(email = email)
    obj.firstname = firstname
    obj.lastname = lastname
    b = {}
    b['user'] = obj
    if obj.password == password:
        if newpassword == confirmnewpassword:
            if newpassword =='':
                obj.save()
            else:     
                obj.password = newpassword
                obj.save()
            return redirect('profile')
        else:
            b['message'] = "The New Password and Confirm New Password don't match!"
            b['firstname']=firstname
            b['lastname']=lastname
            b['email']=email

            return render(request,'notebook/editprofile.html', b)
    else:
        if password == '':
            b['message'] = "Please enter your password !"
        else:
            b['message'] = "Password is incorrect !"
        b['firstname']=firstname
        b['lastname']=lastname
        b['email']=email
        return render(request,'notebook/editprofile.html', b)

def add(request):
    user = UserUn.objects.get(email = request.user.username)
    img = request.FILES.get('img')
    user.img = img
    user.save()
    name = request.FILES.get('img').name
    url = "." + user.img.url
    user.img = uploadFile(name,url)
    user.save()
    return redirect('profile')

def addnotebook(request):
    notebookdatas = NotebookData.objects.all()
    gpus = Gpu.objects.all()
    cpus = Cpu.objects.all()
    rams = Ram.objects.all()
    roms = Rom.objects.all()
    displays = Display.objects.all()
    b = {'notebookdatas':notebookdatas ,'gpus':gpus , 'cpus':cpus , 'rams':rams , 'roms': roms ,'displays': displays}
    if request.method == 'POST':
        notebookdata_id = request.POST['notebookdata']
        gpu_id = request.POST['gpu']
        cpu_id = request.POST['cpu']
        ram_id = request.POST['ram']
        rom_id = request.POST['rom']
        display_id = request.POST['display']
        price = request.POST['price']
        if price!='' and notebookdata_id  != "" and gpu_id != "" and cpu_id != "" and ram_id != "" and rom_id != "" and display_id != "":
            notebookdata = NotebookData.objects.get(id = notebookdata_id)
            gpu = Gpu.objects.get(id = gpu_id)
            cpu = Cpu.objects.get(id = cpu_id)
            ram = Ram.objects.get(id = ram_id)
            rom = Rom.objects.get(id = rom_id)
            display = Display.objects.get(id = display_id)

            n = NoteBook.objects.create(
                notebookdata = notebookdata,
                gpu = gpu,
                cpu = cpu,
                ram = ram,
                rom = rom,
                display = display,
                price = int(price),
                star = (gpu.star + cpu.star + ram.star + rom.star + display.star)/5
                )
            n.save()
            return HttpResponseRedirect(reverse('showadmin'))
        b['err'] = "invalid"
        return render(request,'notebook/addnotebook.html',b)
    return render(request,'notebook/addnotebook.html',b)

def showadmin(request):
    notebookall = NoteBook.objects.all()  
    return render(request,'notebook/admin.html',{"notebookall": notebookall})

def adddatanotebook(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        brand = request.POST['brand']
        descrition = request.POST['descrition']
        typeNotebook = request.POST['typeNotebook']
        series = request.POST['series']
        date = request.POST['date']
        weight = request.POST['weight']
        if brand !='' and descrition != "" and typeNotebook != "" and series != "" and date != "" and weight != "" :
            n = NotebookData.objects.create(img= img,
                brand=brand,
                descrition=descrition,
                typeNotebook=typeNotebook,
                series= series,
                date= date,
                weight=weight
                )
            n.save()
            name = request.FILES.get('img').name
            url = "." + n.img.url
            n.img = uploadFile(name,url)
            n.save()
            return HttpResponseRedirect(reverse('showadmin'))
        return render(request,'notebook/adddatanotebook.html',{"err":"invalid"})
    return render(request,'notebook/adddatanotebook.html')

def addcpu(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        name = request.POST['name']
        star = request.POST['star']
        if brand != "" and name != "" and star != "":
            n = Cpu.objects.create(
                brand= brand,
                name= name,
                star= star,
            )
            n.save()

            return HttpResponseRedirect(reverse('showadmin'))
        return render(request,'notebook/addcpu.html',{"err":"invalid"})
    return render(request,'notebook/addcpu.html')

def addgpu(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        name = request.POST['name']
        star = request.POST['star']
        if brand != "" and name != "" and star != "":
            n = Gpu.objects.create(
                brand= brand,
                name= name,
                star= star,
            )
            n.save()
            return HttpResponseRedirect(reverse('showadmin'))
        return render(request,'notebook/addgpu.html',{"err":"invalid"})
    return render(request,'notebook/addgpu.html')

def addrom(request):
    if request.method == 'POST':
        capacity = request.POST['capacity']
        star = request.POST['star']
        if capacity != "" and star != "":
            n = Rom.objects.create(
                capacity= capacity,
                star= star,
            )
            n.save()
            return HttpResponseRedirect(reverse('showadmin'))
        return render(request,'notebook/addrom.html',{"err":"invalid"})
    return render(request,'notebook/addrom.html')

def addram(request):
    if request.method == 'POST':
        capacity = request.POST['capacity']
        star = request.POST['star']
        if capacity != "" and star != "":
            n = Ram.objects.create(
                capacity= capacity,
                star= star,
            )
            n.save()
            return HttpResponseRedirect(reverse('showadmin'))
        return render(request,'notebook/addram.html',{"err":"invalid"})
    return render(request,'notebook/addram.html')

def adddisplay(request):
    if request.method == 'POST':
        size = request.POST['size']
        resolution = request.POST['resolution']
        star = request.POST['star']
        if size != "" and star != "" and resolution != "" :
            n = Display.objects.create(
                size= size,
                resolution = resolution,
                star= star,
            )
            n.save()
            return HttpResponseRedirect(reverse('showadmin'))
        return render(request,'notebook/adddisplay.html',{"err":"invalid"})
    return render(request,'notebook/adddisplay.html')

def deletenotebook(request):
    notebook_id = request.POST['id']
    n = NoteBook.objects.get(id = notebook_id)
    n.delete()
    return HttpResponseRedirect(reverse('showadmin'))