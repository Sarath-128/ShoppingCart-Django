from django.shortcuts import render
from myapp.models import appl
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import UserProfile, LoginTable
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from cartapp.views import view_card


def list(request):
    apples=appl.objects.all()
    return render(request,'home.html',{'apples':apples})

def Search(request):
    apples=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        apples= appl.objects.filter(Q(item__icontains=query) | Q(price__icontains=query))
    else:
        apples=[]
    context={'apples': apples,'query': query}
    return render(request,'search1.html',context)


def UserReg(request):

    userprofile=UserProfile 
    logintable=LoginTable

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        conf_password=request.POST['conf_password']
        type='user'

        if request.POST['password'] == request.POST['conf_password']:

            userprofile=UserProfile(username=username,password=password,conf_password=conf_password) 
            logintable=LoginTable(username=username,password=password,conf_password=conf_password,type=type)

            
            logintable.save()
            userprofile.save()

            messages.info(request,'Registration Success')
            return redirect('login1')
        else:
            messages.info(request,'Please enter the same password')
            return redirect('register')

    return render(request,'register1.html')

def UserLog(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        

        user=LoginTable.objects.filter(username=username,password=password,type='user').exists()

        try:
            if user is not None:
                user_details = LoginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type == 'user':

                    request.session['username']=user_name
                    return redirect('list')
                
                elif type == 'admin':

                    request.session['username']=user_name
                    return redirect('home')
            else:
                messages.error(request,'Username or password error')
                return redirect('login1')
        
        except LoginTable.DoesNotExist:
            messages.error(request,'Invalid role')
            return redirect('login1')

    return render(request,'login1.html')

def out(request):
    logout(request)
    return redirect('login1')

