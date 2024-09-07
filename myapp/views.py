from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import appl
from .forms import appleForm
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout


# def appMain(request):
#     return render(request,'a.html')

def appMain(request):
    apples=appl.objects.all()

    paginator=Paginator(apples,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
        
    return render(request,'b.html',{'apples': apples,'page':page})


def appleCreate(request):
    apples=appl.objects.all()
    if request.method=='POST':
        apples=appleForm(request.POST,request.FILES)
        if apples.is_valid():
            apples.save()
            return redirect('/')
    else:
        apples=appleForm()
    return render(request,'create.html',{'apples':apples})


def appleUpdate(request,i):
    apples=appl.objects.get(id=i)
    if request.method=='POST':
        apples=appleForm(request.POST,request.FILES,instance=apples)
        if apples.is_valid():
            apples.save()
            return redirect('/')
    else:
        apples=appleForm(instance=apples)
        
    return render(request,'update.html',{'apples':apples})

def Card(request):
    photos=appl.objects.all()

    paginator=Paginator(photos,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'card.html',{'photos':photos,'page':page})


def delete(request,i):
    apples=appl.objects.get(id=i)
    if request.method=='POST':
        apples.delete()
        return redirect('/')
    else:
        apples.delete()
        return redirect('/')


def Search(request):
    apples=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        apples= appl.objects.filter(Q(item__icontains=query) | Q(price__icontains=query))
    else:
        apples=[]
    context={'apples': apples,'query': query}
    return render(request,'search.html',context)

# def Reg(request):

#     if request.method == 'POST':

#         username=request.POST.get('user_name')
#         firstname=request.POST.get('first_name')
#         lastname=request.POST.get('last_name')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         cpassword=request.POST.get('conf_password')
        
#         if password == cpassword :
            
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Entered Username is already taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Entered Email is already taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request,'Entered passwords are not same...')  
#             return redirect('register')      

#     return render(request,'register.html')


# def log(request):
#     if request.method == 'POST':
#         username=request.POST.get('user_name')
#         password=request.POST.get('password')
#         user=auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('home')
#         else:
#             messages.info(request,'Enter valid user')
#             return redirect('login')
#     return render(request,'login.html')

# def logoutUser(request):
#     auth.logout(request)
#     return redirect('login')


