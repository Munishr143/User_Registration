from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

from django.core.mail import send_mail

def Home(request):
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
