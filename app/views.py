
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . form import UserRegisterForm
from django.contrib import messages
from django.views import generic
from .models import Post

class home(generic.ListView):
    template_name = "app/indexpage.html"
    context_object_name = "POST"
    queryset = Post.objects.all()

# def home(request):
#
#     return render(request, 'app/indexpage.html')


def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    context = {'form':form}
    return render(request, 'app/register.html',context)


def demo(request):
    return render(request, 'app/demo.html')


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            print('ok')
            return redirect('app:home')

        else:
            messages.info(request,"Username OR password is incorrect")
            print("Username OR password is incorrect")

    context = {}
    return render(request, 'app/login.html',context)

