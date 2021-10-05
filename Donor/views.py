from django.shortcuts import render,redirect
from django.http import request, HttpResponse
import random
from .models import donor_list,img
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.

def home(request):
    image = img.objects.get(id=1)
    return render(request,'home.html')


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
        donar_details = donor_list.objects.filter(
            name__icontains=search)|donor_list.objects.filter(
            blood__icontains=search)|donor_list.objects.filter(
            age__icontains=search)|donor_list.objects.filter(
            phn__icontains=search)|donor_list.objects.filter(
            gender__startswith=search)
    else:     
        donar_details = donor_list.objects.all()

        # Pagintion
    paginator=Paginator(donar_details,5)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'display.html', {"username" : username,'head': posts_obj})
    else:
      return render(request, 'login.html', {})
    #return render(request, 'display.html', {'head': posts_obj})


    


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
                # messages.info(request,'Email is already in useTaken')
                # 
                return JsonResponse(
                    {'success':'email_check'},
                    safe = False
                )
            else:
                
                user = User.objects.create_user(first_name=name, username=username, password=password1, email=email)
                user.save()
                #return redirect('login')
                return JsonResponse(
                    {'success':'pass'},
                    safe = False
                )
        else:
            #messages.info(request,'Incorrect Password')
            #return redirect('signup')
            return JsonResponse(
                    {'success':'password_check'},
                    safe = False
                )
        #return render(request, 'index.html', {'user': name})

    else:
         return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        check_user = auth.authenticate(username=email, password=password)
        if check_user:
          request.session['username'] = email
         
          return JsonResponse(
               {"success": 'pass'},
               safe=False
             )
        else:
            return JsonResponse(
               {"success": 'error'},
               safe=False)



        # user = auth.authenticate(username=email, password=password)

        # if user is not None:
        #     auth.login(request,user)
        #    # return redirect("/display")
        #     return JsonResponse(
        #        {"success": 'pass'},
        #        safe=False
        #      )
        # else:
        #    # messages.info(request, 'Invalid credentials')
        #    # return redirect("/login")
        #     return JsonResponse(
        #        {"success": 'error'},
        #        safe=False)

    else:
        return render(request, 'login.html')


def logout(request):
    # auth.logout(request)
    try:
        del request.session['username']
    except:
        return redirect('login')

    return redirect("/")
    
    

        


