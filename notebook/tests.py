from django.test import TestCase,Client
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile
class TestAll(TestCase):
    def setUp(self):
        admin = User.objects.create_user(username='admin@admin.com', password='123456tu',is_superuser = 1)
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
        ''''''
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


    
    def test_index_url(self):
        """ เข้าหน้าindex """ 
        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')


    
    def test_index_url_login(self):
        """ เข้าหน้าindexเเบบlogin """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('index'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    def test_index_sort(self):
        """ ทดสอบ กดเรียงเเบบ Newest  """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'sort','sortNotebook':'Newest'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    def test_index_sort2(self):
        """ ทดสอบ กดเรียงเเบบ Oldest  """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'sort','sortNotebook':'Oldest'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')
    
    def test_index_sort3(self):
        """ ทดสอบ กดเรียงเเบบ Highest price """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'sort','sortNotebook':'Highest price'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')
        
    def test_index_sort4(self):
        """ ทดสอบ กดเรียงเเบบ Lowest price """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'sort','sortNotebook':'Lowest price'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    
    def test_index_search1(self):
        """ เข้าหน้าindexแบบsearchเจอ1ตัว """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'search','input1':'nitro'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    
    def test_index_search2(self):
        """ เข้าหน้าindexแบบsearch """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'search','input1':'acer'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')

    
    def test_index_search3(self):
        """ เข้าหน้าindexแบบsearch เเต่ไม่เจอ """
        c = Client()
        response = c.post(reverse('index'),data = {'form':'search','input1':'eeeeee'})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/index.html')
    
    #กดlogin(addfail)
    def test_login_url_fail(self):
        """ กดlogin ใส่ข้อมูลผิด """
        c = Client()
        response = c.post(reverse("login"),data={'username':'eknarin@gmail.com','password':'123456'})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'notebook/login.html')
    
    
    def test_login(self):
        """ กดlogin ใส่ข้อมูลถูก"""
        c = Client()
        response = c.post(reverse('login'),data={'username':'eknarin@gmail.com','password':'123456tu'})
        self.assertEqual(response.status_code,302)
    
    def test_login_notpost(self):
        """ กดloginโดยไม่post """
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'notebook/login.html')

    
    def test_Loginpage_url(self):
        """ กดไปหน้า login pange"""
        c = Client()
        response = c.get(reverse('login_logoutpage'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/login.html')
    
    
    def test_Logoutpage_url(self):
        """ กด logout """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('login_logoutpage'))
        self.assertEqual(response.status_code,302)
    
    
    def test_register_url(self):
        """ ไปหน้าregister """
        c = Client()
        response = c.get(reverse('register'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
    

    
    def test_addregister_nopost(self):
        """ ไปหน้าaddregister ต้องกลับมาหน้า regiter """
        c = Client()
        response=c.get(reverse('addregister'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
    
    
    def test_addregister_url(self):
        """ registerเเบบpostถูกต้อง """
        c = Client()
        response = c.post(reverse('addregister'),data={"firstname":"aa","lastname":"bb","email":"aa@bb.com","password":"123456","confirmpassword":"123456"})
        self.assertEqual( response.status_code,200)
        self.assertEqual(UserUn.objects.all().count() , 4)
        self.assertTemplateUsed(response ,'notebook/login.html')
    
    #registerเเบบpostเเบบไม่ถูกต้อง
    def test_addregister_url_fail(self):
        """  registerเเบบpostแบบไม่ถูกต้อง """
        c = Client()
        response = c.post(reverse('addregister'),data={"firstname":"","lastname":"","email":"","password":"","confirmpassword":""})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
        self.assertEqual(UserUn.objects.all().count() , 3)
    
    
    def test_addregister_url_fail_2(self):
        """ registerggเเบบลงชื่อซ้ำ """
        c = Client()
        response = c.post(reverse('addregister'),data={"firstname":"eknarin","lastname":"lerdnuntawat","email":"eknarin@gmail.com","password":"123456tu","confirmpassword":"123456tu"})
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
        self.assertEqual(UserUn.objects.all().count() , 3)
    
    def test_addregister_fail(self):
        """ registerggเเบบไม่ถูกต้องpasswordผิด """
        c = Client()
        response = c.post('/addregister',data={"firstname":"a","lastname":"b","email":"a@b.com","password":"123","confirmpassword":"1"})
        self.assertEqual( response.status_code,200)
        self.assertEqual(UserUn.objects.all().count() , 3)
        self.assertTemplateUsed(response ,'notebook/register.html')

    def test_about_url(self):
        """ ไปหน้าabout """
        c = Client()
        response = c.get(reverse('about'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/about.html')
    

    def test_favorite_url(self):
        """ ไปหน้าfavorite ยังไม่ได้login """
        c = Client()
        response = c.get(reverse('favorite'))
        self.assertEqual(response.status_code,200)
    
    
    def test_favorite_url_login(self):
        """  ไปหน้าfavorite loginแล้ว  """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('favorite'))
        self.assertEqual(response.status_code,200)
    
    def test_notebook_url(self):
        """  ไปหน้าเเสดง notebook ไม่post"""
        c = Client()
        response = c.get(reverse('notebook'))
        self.assertEqual(response.status_code,302)
    
  
    def test_notebook_url_post(self):
        """ ไปหน้าเเสดง notebook เเบบpost """
        c = Client()
        response = c.post(reverse('notebook'),data={'notebook_id':1})
        self.assertEqual(response.status_code,200)
    
    
    def test_compare(self):
        """ ไปหน้าเเสดงcompare """
        c = Client()
        response = c.get(reverse('compare'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/compare.html')
    

    def test_removecompare(self):
        """ ลบnotebook compare """
        c = Client()
        response = c.post(reverse('removecompare'),data={'rmcompare':1})
        self.assertEqual(response.status_code,302)
    
    def test_calcompare_noadd(self):
        """ เพิ่มnotebook compare """
        c = Client()
        response = c.post(reverse('calcompare'),data={'notebook_id':1})
        self.assertEqual(response.status_code,302)
    
    def test_calcompare_add(self):
        """ เพิ่มnotebook compare """
        c = Client()
        response = c.post(reverse('calcompare'),data={'notebook_id':2})
        self.assertEqual(response.status_code,302)

    def test_mark(self):
        """ เพิ่มnotebook เเบบget """
        c =Client()
        response = c.get(reverse('mark'))
        self.assertEqual(response.status_code,302)
    
    def test_mark_post(self):
        """ เพิ่ม notebook ที่ถูกใจ """
        c =Client()
        response = c.post(reverse('mark'),)
        self.assertEqual(response.status_code,200)
    
    def test_mark_post_login_add(self):
        """ """
        c =Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('mark'),data={'id':1})
        self.assertEqual(response.status_code,302)

    def test_mark_post_login_noadd(self):
        """  เพิ่มnotebook เเบบ login """
        c =Client()
        c.login(username='mata@gmail.com', password='123456tu')
        mata = UserUn.objects.get(email= "mata@gmail.com")
        note = NoteBook.objects.get(id = 1)
        mata.favorite.add(note)
        response = c.post(reverse('mark'),data={'id':1})
        self.assertEqual(response.status_code,302)
    
    def test_unmarkfav(self):
        """ ลบnotebook เเบบ login เเต่ไม่post """
        c =Client()
        response = c.get(reverse('unmarkfav'))
        self.assertEqual(response.status_code,302)
    
    def test_unmarkfav_post(self):
        """  ลบnotebook เเบบ login """
        c =Client()
        c.login(username='eknarin@gmail.com', password='123456tu')
        response = c.post(reverse('unmarkfav'),data={'id':1})
        self.assertEqual(response.status_code,302)
    def test_filter_post(self):
        """ กด เลือก filter ที่ต้องการ"""
        c =Client()
        response = c.post(reverse('filter'),data={'form':'filter','typeNotebook': 'Gamimg'})
        self.assertEqual(response.status_code,200)
    
    def test_profile(self):
        """ ไปหน้าprofile """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        mata = UserUn.objects.get(email= "mata@gmail.com")
        response = c.get(reverse('profile'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/profile.html')
    
    def test_editprofile(self):
        """ ไปหน้า editprofile"""
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('editprofile'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/editprofile.html')
    
    def test_editprofilevalue(self):
        """ ส่งค่าeditprofile เเก้ชื่อ  """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('editprofilevalue'), data={'firstname': 'mata' ,'lastname': 'mata','password': '123456tu','newpassword': '','confirmnewpassword': ''  } )
        self.assertEqual(response.status_code,302)
    def test_editprofilevalue_password(self):
        """ ส่งค่าeditprofile เเก้password"""
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('editprofilevalue'), data={'firstname': 'mata' ,'lastname': 'mata','password': '123456tu','newpassword': '123456tu','confirmnewpassword': '123456tu'  } )
        self.assertEqual(response.status_code,302)
    
    def test_editprofilevalue_password_err(self):
        """ ส่งค่าeditprofile เเก้ชื่อ ใส่ระหัสผิด """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('editprofilevalue'), data={'firstname': 'mata' ,'lastname': 'mata','password': '123456tu','newpassword': '123456tu','confirmnewpassword': '123456'  } )
        self.assertEqual(response.status_code,200)
    
    def test_editprofilevalue_password_err_invalid(self):
        """ ส่งค่าeditprofile ใส่รหัสผิด"""
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('editprofilevalue'), data={'firstname': 'mata' ,'lastname': 'mata','password': '123456','newpassword': '123456tu','confirmnewpassword': '123456'  } )
        self.assertEqual(response.status_code,200)
    
    def test_editprofilevalue_password_null(self):
        """ส่งค่าeditprofile ไม่ได้ใส่รหัส  """
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('editprofilevalue'), data={'firstname': 'mata' ,'lastname': 'mata','password': '','newpassword': '123456tu','confirmnewpassword': '123456'  } )
        self.assertEqual(response.status_code,200)
    
    def test_addnotebook_get(self):
        """ ไปหน้า เเอดโน็ตบุคของadmin """
        c = Client()
        response = c.get(reverse('addnotebook'))
        self.assertEqual(response.status_code,200)
    
    def test_addnotebook(self):
        """ เพิ่มnotebook ลงdatabase """
        c = Client()
        response = c.post(reverse('addnotebook'), data= {'notebookdata' :'1',
            "cpu": '1',
            "gpu": '1',
            "ram": '1',
            "rom": '1',
            "display": '1',
            "price" : '35900'})
        self.assertEqual(response.status_code,302)
    
    def test_addnotebook_invalid(self):
        """ เพิ่มnotebook ลงdatabase ไม่ได้กรอกข้อมูล"""
        c = Client()
        response = c.post(reverse('addnotebook'), data= {'notebookdata' :'1',
            "cpu": '',
            "gpu": '',
            "ram": '',
            "rom": '',
            "display": '',
            "price" : ''})
        self.assertEqual(response.status_code,200)
    
    
    def test_showadmin(self):
        """ เไปเเสดงหน้า admin"""
        c = Client()
        response = c.get(reverse('showadmin'))
        self.assertEqual(response.status_code,200)
    
    def test_add(self):
        """ เเก้รูป โปรไฟล์"""
        url = "/Users/ACER/Desktop/cn331/unnaidee/notebook/static/img/"
        img = open(url+'shop01.png','rb')
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('add'),data={'img' : img} )
        self.assertEqual(response.status_code,302)

    def test_adddatanotebook_import(self):
        """ ใส่ข้อมูลdatanotebook """
        url = "/Users/ACER/Desktop/cn331/unnaidee/notebook/static/img/"
        img = open(url+'shop01.png','rb')
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('adddatanotebook'),data={'img' : img ,
                                                "brand":"acer",
                                                 "descrition":"the best gaming",
                                                 "typeNotebook":"gaming",
                                                 "series":"nitro5",
                                                 "date":"2020-04-28",
                                                 "weight": "2.6"} )
        self.assertEqual(response.status_code,302)

    def test_adddatanotebook_import_invalid(self):
        """ ใส่ข้อมูลdatanotebookผิด """
        url = "/Users/ACER/Desktop/cn331/unnaidee/notebook/static/img/"
        img = open(url+'shop01.png','rb')
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.post(reverse('adddatanotebook'),data={'img' : img ,
                                                "brand":"",
                                                 "descrition":"",
                                                 "typeNotebook":"",
                                                 "series":"",
                                                 "date":"",
                                                 "weight": ""} )
        self.assertEqual(response.status_code,200)
    
    def test_adddatanotebook_get(self):
        """ ไปหน้าadddatanotebook """
        c = Client()
        response = c.get(reverse('adddatanotebook'))
        self.assertEqual(response.status_code,200)
    
    def test_addcpu_get(self):
        """ ไปหน้า addcpu """
        c = Client()
        response = c.get(reverse('addcpu'))
        self.assertEqual(response.status_code,200)
    
    def test_addcpu_post(self):
        """ เพิ่ม cpu """
        c = Client()
        response = c.post(reverse('addcpu'),data = {"brand":"intel","name":"Core i5 10300H","star":"4"})
        self.assertEqual(response.status_code,302)

    def test_addcpu_post_invalid(self):
        """ ใส่ข้อมูลcpuผิด """
        c = Client()
        response = c.post(reverse('addcpu'),data = {"brand":"","name":"","star":""})
        self.assertEqual(response.status_code,200)


    def test_addgpu_get(self):
        """ไปหน้า addgpu """
        c = Client()
        response = c.get(reverse('addgpu'))
        self.assertEqual(response.status_code,200)
    
    def test_addgpu_post(self):
        """ เพิ่ม gpu"""
        c = Client()
        response = c.post(reverse('addgpu'),data = {"brand":"Nvidia","name":"RTX2060","star":"5"})
        self.assertEqual(response.status_code,302)
    
    def test_addgpu_post_invalid(self):
        """ ใส่ข้อมูล addgpu """
        c = Client()
        response = c.post(reverse('addgpu'),data = {"brand":"","name":"","star":""})
        self.assertEqual(response.status_code,200)
    
    def test_addrom_get(self):
        """ ไปหน้า addrom"""
        c = Client()
        response = c.get(reverse('addrom'))
        self.assertEqual(response.status_code,200)
    
    def test_addrom_post(self):
        """ ใส่ข้อมูล rom"""
        c = Client()
        response = c.post(reverse('addrom'),data = {"capacity":"512","star":"5"})
        self.assertEqual(response.status_code,302)
    
    def test_addrom_post_invalid(self):
        """ ใส่ข้อมูลromผิด """
        c = Client()
        response = c.post(reverse('addrom'),data = {"capacity":"","star":""})
        self.assertEqual(response.status_code,200)
    
    def test_addram_get(self):
        """ ไปหน้า addram"""
        c = Client()
        response = c.get(reverse('addram'))
        self.assertEqual(response.status_code,200)
    
    def test_addram_post(self):
        """ ใส่ข้อมูลram"""
        c = Client()
        response = c.post(reverse('addram'),data = {"capacity":"8","star":"5"})
        self.assertEqual(response.status_code,302)
    
    def test_addram_post_invalid(self):
        """ ใส่ข้อมูลram ผิด """
        c = Client()
        response = c.post(reverse('addram'),data = {"capacity":"","star":""})
        self.assertEqual(response.status_code,200)
    
    def test_adddisplay_get(self):
        """ ไปหน้า adddisplay """
        c = Client()
        response = c.get(reverse('adddisplay'))
        self.assertEqual(response.status_code,200)
    
    def test_adddisplay_post(self):
        """ ใส่ข้อมูล display """
        c = Client()
        response = c.post(reverse('adddisplay'),data = {"size":"15.6","resolution":"1920X1080 @144FPS","star":"5"})
        self.assertEqual(response.status_code,302)
    
    def test_adddisplay_post_invalid(self):
        """ ใส่ข้อมูล display """
        c = Client()
        response = c.post(reverse('adddisplay'),data = {"size":"","resolution":"","star":""})
        self.assertEqual(response.status_code,200)
    def test_deletenotebook(self):
        """ ลบnotebook ออกจากdatabase"""
        c = Client()
        response = c.post(reverse('deletenotebook'),data = {"id":"1"})
        self.assertEqual(response.status_code,302)
    #กดlogin_page(เข้าระบบได้ได้)
    def test_loginadmin(self):
        """ login ในฐานะaadmin """
        c = Client()
        response = c.post(reverse('login'),data={'username':'admin@admin.com','password':'123456tu'})
        self.assertEqual(response.status_code,302)




