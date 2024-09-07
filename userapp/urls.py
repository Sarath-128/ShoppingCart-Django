from django.contrib import admin
from django.urls import path,include
from . import views
 

urlpatterns = [
    
    path('www/',views.list,name='list'),
    path('searc/',views.Search,name='search'),

    path('register',views.UserReg,name="register"),
    path('',views.UserLog,name='login1'),
    path('logout/',views.out,name="logout")
 
]