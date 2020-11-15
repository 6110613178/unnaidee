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
    path('search',views.search, name='search'),
]