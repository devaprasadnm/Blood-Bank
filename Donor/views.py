from django.shortcuts import render,redirect
from django.http import request, HttpResponse
import random
from .models import donor_list,img
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    image = img.objects.get(id=1)
    return render(request)


def form(request):
    if request.method == 'POST':

        donar_details =  donor_list()
        
        donar_details.name = request.POST['name']
        donar_details.email = request.POST['email']
        donar_details.phn = request.POST['phn']
        donar_details.blood = request.POST['blood']
        donar_details.age = request.POST['age']
        donar_details.gender = request.POST['gender']
          
        donar_details.save()
    
        return redirect("/display")
   
    else :
        return render(request, 'index.html')


def display(request):
    if request.method == 'POST':
        search =  request.POST['q'] 
        donar_details = donor_list.objects.filter(name__icontains=search)
    else:     
        donar_details = donor_list.objects.all()

        # Pagintion
    paginator=Paginator(donar_details,5)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request, 'display.html', {'head': posts_obj})


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password1 = request.POST['password']
        password2 = request.POST['repassword']
        email = request.POST['email']
        username = str(email)
        global id
        id =email
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already in useTaken')
                return redirect('signup')
            else:
                
                user = User.objects.create_user(first_name=name, username=username, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Incorrect Password')
            return redirect('signup')
        return render(request, 'index.html', {'user': name})

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            global id
            id = email
            auth.login(request,user)
            return redirect("/display")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect("/login")

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
    
    
        


