from django.test import TestCase,Client
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserUn
class TestAll(TestCase):
    def setUp(self):
        user_1 = User.objects.create_user(username='eknarin@gmail.com', password='123456tu')
        user_2 = User.objects.create_user(username='mata@gmail.com', password='123456tu')
        user_3 = User.objects.create_user(username='tham@gmail.com', password='123456tu')
        
        userun_1 = UserUn.objects.create(firstname= 'eknarin',lastname= 'lerdnuntawat', email= 'eknarin@gmail.com',password='123456tu')
        userun_2 = UserUn.objects.create(firstname= 'mata', lastname = 'mt',email='mata@gmail.com',password='123456tu')
        userun_3 = UserUn.objects.create(firstname= 'tham',lastname='th',email='tham@gmil.com',password='123456tu')



    def testindex(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual( response.status_code,200)
    def testLogin(self):
        c = Client()
        response = c.get(reverse('login_logoutpage'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/login.html')
    
    def testLogout(self):
        c = Client()
        c.login(username='mata@gmail.com', password='123456tu')
        response = c.get(reverse('login_logoutpage'))
        self.assertEqual(response.status_code,302)
    def testregister(self):
        c = Client()
        response = c.get(reverse('register'))
        self.assertEqual( response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/register.html')
    def testaddregister(self):
        c = Client()
        response = c.get(reverse('addregister'))
        self.assertEqual( response.status_code,200)
    def testabout(self):
        c = Client()
        response = c.get(reverse('about'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response ,'notebook/about.html')
        
    def testuser(self):
        userun_test = UserUn.objects.get(email="eknarin@gmail.com")
        c = userun_test.favarite.count()
        self.assertEqual(c, 0) 


        