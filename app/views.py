from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request, 'home.html', d)
    return render(request, 'home.html')

def Registration(request):
    UFO=User_Form()
    PFO=Profile_Form()
    d={'UFO':UFO, 'PFO':PFO}

    if request.method=='POST' and request.FILES:
        UFD=User_Form(request.POST)
        PFD=Profile_Form(request.POST, request.FILES)

        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            NSUO.set_password(UFD.cleaned_data['password'])
            NSUO.save()

            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()

            send_mail('Registration', 
                      'Sucessfully Registration is done', 
                      'munishr428@gmail.com', 
                      [NSUO.email], 
                      fail_silently=False)
            return HttpResponse('Registered Sucessfully')
        else:
            return HttpResponse('Data is not Valid')


    return render(request, 'registration.html', d)

def User_Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username, password=password)

        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        
        else:
            return HttpResponse('Invalid username or password')


    return render(request, 'User_Login.html')

@login_required
def User_Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))