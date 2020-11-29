from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('about',views.about, name = 'about'),
    path('register',views.register, name = 'register'),
    path('addregister',views.addregister, name = 'addregister'),
    path('login_logoutpage',views.login_logoutpage, name='login_logoutpage'),
    path('login',views.login_view, name='login'),
    path('compare',views.compare, name='compare'),
    path('calcompare',views.calcompare, name='calcompare'),
    path('removecompare',views.removecompare, name='removecompare'),
    path('mark',views.mark, name='mark'),
    path('favorite',views.favorite, name='favorite'),
    path('unmarkfav',views.unmarkfav, name='unmarkfav'),
    path('notebook',views.notebook_page,name = 'notebook'),
    path('search',views.index, name='search'),
    path('filter',views.index,name = 'filter'),
    path('sort',views.index,name = 'sort'),
    path('profile',views.profile,name = 'profile'),
    path('editprofile',views.editprofile,name = 'editprofile'),
    path('editprofilevalue',views.editprofilevalue,name = 'editprofilevalue'),
    path('add',views.add,name = 'add'),
    path('addnotebook',views.addnotebook, name = 'addnotebook'),
    path('showadmin',views.showadmin, name = 'showadmin'),
    path('adddatanotebook',views.adddatanotebook, name = 'adddatanotebook'),
    path('addcpu',views.addcpu, name = 'addcpu'),
    path('addgpu',views.addgpu, name = 'addgpu'),
    path('addrom',views.addrom, name = 'addrom'),
    path('addram',views.addram, name = 'addram'),
    path('adddisplay',views.adddisplay, name = 'adddisplay'),
    path('deletenotebook',views.deletenotebook, name = 'deletenotebook'),



]