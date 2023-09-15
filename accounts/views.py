from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile

# Create your views here.

def log_in(request):

    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        usr_obj =  User.objects.filter(username = email)
        
        if  not usr_obj.exists():
            messages.warning(request, "Account not Found")
            return HttpResponsePermanentRedirect(request.path_info)
        
        
        if not usr_obj[0].profile.is_email_verifed:
             messages.warning(request, "Your email not varifed")
             return HttpResponsePermanentRedirect(request.path_info)
        
        user_obj = authenticate(username = email, password= password)

        # if user_obj:
             
        
             
           
        # messages.success(request, "An email has been sent on your email")
        
    return render(request, 'accounts/login.html')


def signUp(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email  = request.POST['email']
        password = request.POST['password']
        
        usr_obj =  User.objects.filter(username = email)
        
        if  usr_obj.exists():
            messages.warning(request, "Email is already exist")
            return HttpResponsePermanentRedirect(request.path_info)
             
             
        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "An email has been sent on your email")
        
    return render(request, 'accounts/register.html')