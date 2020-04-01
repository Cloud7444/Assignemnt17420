
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from . form import UserRegisterForm


def home(request):
    return render(request, 'app/indexpage.html')

def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'app/register.html',context)

def demo(request):
    return render(request, 'app/demo.html')

def login(request):
    return render(request, 'app/login.html')
