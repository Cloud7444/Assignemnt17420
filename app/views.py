from audioop import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate


def home(request):
    return render(request, 'app/indexpage.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(user)
            return redirect("app/demo.html")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,
                  'app/register.html',
                  context={"form":form})

def demo(request):
    return render(request, 'app/demo.html')

def login(request):
    return render(request, 'app/login.html')
