from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Login(request):
    return render(request, 'login.html')
def About(request):
    return render(request, 'about.html')
def Home(request):
    return render(request, 'home.html')