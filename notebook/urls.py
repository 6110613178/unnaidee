from django.urls import path
from . import views
urlpatterns = [
     path('',views.index, name = "index"),
    path('about',views.about, name = 'about'),
    path('register',views.register, name = 'register'),
    path('addregister',views.addregister, name = 'addregister'),
    path('login_logoutpage',views.login_logoutpage, name='login_logoutpage'),
    path('login',views.login_view, name='login'),
    path('compare',views.compare, name='compare'),
]