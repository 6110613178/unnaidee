from django.test import TestCase,Client
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
class TestAll(TestCase):
    def setUp(self):
        user_1 = User.objects.create_user(username='eknarin@gmail.com', password='123456tu')
        user_2 = User.objects.create_user(username='mata@gmail.com', password='123456tu')
        user_3 = User.objects.create_user(username='tham@gmail.com', password='123456tu')
        
        userun_1 = UserUn.objects.create(firstname= 'eknarin',lastname= 'lerdnuntawat', email= 'eknarin@gmail.com',password='123456tu')
        userun_2 = UserUn.objects.create(firstname= 'mata', lastname = 'mt',email='mata@gmail.com',password='123456tu')
        userun_3 = UserUn.objects.create(firstname= 'tham',lastname='th',email='tham@gmil.com',password='123456tu')
        #data
        nitro5 = NotebookData.objects.create(brand="acer", descrition="the best gaming",typeNotebook="gaming",series="nitro5",date="2020-04-28")
        swift3 = NotebookData.objects.create(brand="acer", descrition="the best working",typeNotebook="working",series="swift3",date="2020-04-28")
        modern15 = NotebookData.objects.create(brand="msi", descrition="the best working",typeNotebook="working",series="modern15",date="2020-04-28")
        #Ram
        ram8 = Ram.objects.create(capacity="8 GB",star=3)
        ram16 = Ram.objects.create(capacity="16 GB",star=5) 
        #Rom
        rom512 = Rom.objects.create(capacity="512 GB",star=4)
        #GPU
        rtx2060 = Gpu.objects.create(brand="Nvidia",name="RTX2060",star=5)
        mx250 = Gpu.objects.create(brand="Nvidia",name="MX250",star=2)
        mx350 = Gpu.objects.create(brand="Nvidia",name="MX350",star=3)
        #CPU
        i5_10300h = Cpu.objects.create(brand="intel",name="Core i5 10300H",star=4)
        i5_10210u = Cpu.objects.create(brand="intel",name="Core i5 10210U",star=2)
        i5_1035G1 = Cpu.objects.create(brand="intel",name="Core i5 1035G1",star=2)
        #Display
        inch14 = Display.objects.create(size="14",resolution="1920X1080 @60FPS",star=3)
        inch15 = Display.objects.create(size="15.6",resolution="1920X1080 @60FPS",star=4)
        inch15_144hz = Display.objects.create(size="15.6",resolution="1920X1080 @144FPS",star=5)       
        #Notebook
        Acer_Nitro5 = NoteBook.objects.create(
            notebookdata=nitro5,
            cpu=i5_10300h,
            gpu=rtx2060,
            ram=ram16,
            rom=rom512,
            display=inch15_144hz,
            price=35900
            )
        Acer_Swift3 = NoteBook.objects.create(
            notebookdata=swift3,
            cpu=i5_1035G1,
            gpu=mx250,
            ram=ram8,
            rom=rom512,
            display=inch14,
            price=27900
            )
        Msi_Modern15 = NoteBook.objects.create(
            notebookdata=modern15,
            cpu=i5_10210u,
            gpu=mx350,
            ram=ram16,
            rom=rom512,
            display=inch15,
            price=29900
            )
        userun_1.favorite.add(Acer_Nitro5)

        compare = Compare.objects.create(allstar=4.0,notebook = Acer_Nitro5)
    

    def test_model(self):
        nitro  = NotebookData.objects.get(series= 'nitro5')
        userun1 = UserUn.objects.get(firstname= 'eknarin')
        ram = Ram.objects.get(id = 1)
        rom = Rom.objects.get(id = 1)
        cpu = Cpu.objects.get(id = 1)
        gpu = Gpu.objects.get(id = 1)
        display = Display.objects.get(id = 1)
        notebook = NoteBook.objects.get(id = 1)
        compare = Compare.objects.get(id =1)
        self.addTypeEqualityFunc(str,nitro.__str__())
        self.addTypeEqualityFunc(str,userun1.__str__())
        self.addTypeEqualityFunc(str,ram.__str__())
        self.addTypeEqualityFunc(str,rom.__str__())
        self.addTypeEqualityFunc(str,gpu.__str__())
        self.addTypeEqualityFunc(str,cpu.__str__())
        self.addTypeEqualityFunc(str,display.__str__())
        self.addTypeEqualityFunc(str,notebook.__str__())
        self.addTypeEqualityFunc(str,compare.__str__())


    #เข้าหน้าindex_url
    def test_index_url(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')


     #เข้าหน้าindex_url
    def test_index_url_login(self):
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('index'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')
    
    #เข้าหน้าindexแบบsearchเจอ1ตัว
    def test_index_search1(self):
        c = Client()
        response = c.post(reverse('index'),data = {'form':'search','input1':'nitro'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    #เข้าหน้าindexแบบsearch
    def test_index_search2(self):
        c = Client()
        response = c.post(reverse('index'),data = {'form':'search','input1':'acer'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    #เข้าหน้าindexแบบsearch
    def test_index_search3(self):
        c = Client()
        response = c.post(reverse('index'),data = {'form':'search','input1':'eeeeee'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')
    
    #กดlogin(addfail)
    def test_login_url_fail(self):
        c = Client()
        response = c.post(reverse("login"),data={'username':'eknarin@gmail.com','password':'123456'})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'notebook/login.html')
    
    #กดlogin_page(เข้าระบบได้ได้)
    def test_login(self):
        c = Client()
        response = c.post(reverse('login'),data={'username':'eknarin@gmail.com','password':'123456tu'})
        self.assertEqual(response.status_code,302)
    
    #กดloginโดยไม่post
    def test_login_notpost(self):
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'notebook/login.html')

    #กดlogin(fail)เพราะซ้ำ
    def test_login_fail(self):
        c = Client()
        response = c.post(reverse('login'),data={'username':'eknarin@gmail.com','password':'123456'})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'notebook/login.html')
    
    
    #กดไปหน้า login แบบreverse
    def test_Loginpage_url(self):
        c = Client()
        response = c.get(reverse('login_logoutpage'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/login.html')
    
    #กด logout แบบreverse
    def test_Logoutpage_url(self):
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('login_logoutpage'))
        self.assertEqual(response.status_code,302)
    
    #ไปหน้าregisterแบบ reverse
    def test_register_url(self):
        c = Client()
        response = c.get(reverse('register'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
    

    #ไปหน้าregisterแบบไม่post
    def test_register_nopost(self):
        c = Client()
        response=c.get(reverse('addregister'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
    
    #registerเเบบpostถูกต้อง
    def test_addregister_url(self):
        c = Client()
        response = c.post(reverse('addregister'),data={"firstname":"aa","lastname":"bb","email":"aa@bb.com","password":"123456","confirmpassword":"123456"})
        self.assertEqual( response.status_code,200)
        self.assertEqual(UserUn.objects.all().count() , 4)
        self.assertTemplateUsed(response ,'notebook/login.html')
    
    #registerเเบบpostเเบบไม่ถูกต้อง
    def test_addregister_url_fail(self):
        c = Client()
        response = c.post(reverse('addregister'),data={"firstname":"","lastname":"","email":"","password":"","confirmpassword":""})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
        self.assertEqual(UserUn.objects.all().count() , 3)
    
    #registerggเเบบไม่ถูกต้อง2ซ้ำ
    def test_addregister_url_fail_2(self):
        c = Client()
        response = c.post(reverse('addregister'),data={"firstname":"eknarin","lastname":"lerdnuntawat","email":"eknarin@gmail.com","password":"123456tu","confirmpassword":"123456tu"})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
        self.assertEqual(UserUn.objects.all().count() , 3)
    #registerggเเบบไม่ถูกต้อง2
    def test_addregister_fail(self):
        c = Client()
        response = c.post('/addregister',data={"firstname":"a","lastname":"b","email":"a@b.com","password":"123","confirmpassword":"1"})
        self.assertEqual( response.status_code,200)
        self.assertEqual(UserUn.objects.all().count() , 3)
        self.assertTemplateUsed(response ,'notebook/register.html')
    #ไปหน้าabout
    def test_about_url(self):
        c = Client()
        response = c.get(reverse('about'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/about.html')
    
    #ไปหน้าfavorite
    def test_favorite_url(self):
        c = Client()
        response = c.get(reverse('favorite'))
        self.assertEqual(response.status_code,200)
    
    def test_favorite_url_login(self):
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('favorite'))
        self.assertEqual(response.status_code,200)
    
    #ไปหน้าเเสดง note
    def test_notebook_url(self):
        c = Client()
        response = c.get(reverse('notebook'))
        self.assertEqual(response.status_code,302)
    
    #ไปหน้าเเสดง note
    def test_notebook_url_post(self):
        c = Client()
        response = c.post(reverse('notebook'),data={'notebook_id':1})
        self.assertEqual(response.status_code,200)
    
    #ไปหน้าเเสดงcompare
    def test_compare(self):
        c = Client()
        response = c.get(reverse('compare'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/compare.html')
    #ไปหน้า calcompare
    

    def test_removecompare(self):
        c = Client()
        response = c.post(reverse('removecompare'),data={'rmcompare':1})
        self.assertEqual(response.status_code,302)
    
    def test_calcompare_noadd(self):
        c = Client()
        response = c.post(reverse('calcompare'),data={'notebook_id':1})
        self.assertEqual(response.status_code,302)
    
    def test_calcompare_add(self):
        c = Client()
        response = c.post(reverse('calcompare'),data={'notebook_id':2})
        self.assertEqual(response.status_code,302)

    def test_mark(self):
        c =Client()
        response = c.get(reverse('mark'))
        self.assertEqual(response.status_code,302)
    
    def test_mark_post(self):
        c =Client()
        response = c.post(reverse('mark'),)
        self.assertEqual(response.status_code,200)
    
    def test_mark_post_login_add(self):
        c =Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('mark'),data={'id':1})
        self.assertEqual(response.status_code,302)

    def test_mark_post_login_noadd(self):
        c =Client()
        c.login(username='mata@gmail.com', password='123456tu')
        mata = UserUn.objects.get(email= "mata@gmail.com")
        note = NoteBook.objects.get(id = 1)
        mata.favorite.add(note)
        response = c.post(reverse('mark'),data={'id':1})
        self.assertEqual(response.status_code,302)
    
    def test_unmarkfav(self):
        c =Client()
        response = c.get(reverse('unmarkfav'))
        self.assertEqual(response.status_code,302)
    
    def test_unmarkfav_post(self):
        c =Client()
        c.login(username='eknarin@gmail.com', password='123456tu')
        response = c.post(reverse('unmarkfav'),data={'id':1})
        self.assertEqual(response.status_code,302)
    def test_filter_post(self):
        c =Client()
        response = c.post(reverse('filter'),data={'form':'filter','typeNotebook': 'Gamimg'})
        self.assertEqual(response.status_code,200)