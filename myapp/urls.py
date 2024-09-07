
from django.urls import path
from . import views


urlpatterns = [
    
    path('home/',views.appMain,name='home'),
    path('create/',views.appleCreate,name='create'),
    path('Update/<int:i>/',views.appleUpdate,name='update'),
    path('card/',views.Card,name='card'),
    path('del/<int:i>',views.delete,name='del'),
    path('search/',views.Search,name='search'),
    # path('register/',views.Reg,name='register'),
    # path('',views.log,name='login'),
    # path('logout/',views.logoutUser,name="logout")
]