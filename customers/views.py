from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
# Create your views here.
def account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            #Creating user acc
            user=User.objects.create(
                username=username,
                password=password,
                email=email
            )
            Customer.objects.create(
                user=user
            )
            return redirect('home')
        except Exception as e:
            error_message = "Duplicate credentials"
            messages.error(request,error_message)

    elif request.POST and 'login' in request.POST:
        pass
    return render(request,'account.html')