from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import datas #database name datas
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
def home(req):
    return render(req,'home.html')
    
def login(req):
    return render(req,'login.html')

def register(req):
    form=CreateUserForm()
    return render(req,'register.html',{'form':form})
