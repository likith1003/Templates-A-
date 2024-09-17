from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse('Welcome to Home Page')
    return render(request, 'home.html')


def login(request):
    # return HttpResponse('Welcome to Login Page')
    return render(request, 'login.html')


def register(request):
    # return HttpResponse('Welcome to register Page')
    return render(request, 'register.html')
