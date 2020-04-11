
from django.shortcuts import render, redirect ,HttpResponse, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from . form import UserRegisterForm ,ListAuthor
from django.contrib import messages

from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def register(request):
    if request.user.is_authenticated:
        return redirect('app:home')
    else:
        form = UserRegisterForm()
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                return redirect('app:login')
            else:
                messages.success(request, 'not works')
        context = {'form':form}
        return render(request, 'app/register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('app:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('app:home')

            else:
                messages.info(request,"Username OR password is incorrect")


        context = {}
        return render(request, 'app/login.html',context)


def logoutpage(request):
    logout(request)
    return redirect('app:login')


@login_required(login_url='app:login')
def postview(request):
    # if request.user.is_staff==True:
        allposts = Post.objects.all()
        return render(request,'app/indexpage.html',
                      {'allPost' : allposts})
    # else:
    #     return redirect('app:userpage')


def userpage(request):
    return render(request, 'app/indexpage.html')

@login_required(login_url='app:login')
def updatepost(request,pk):
    instance = Post.objects.get(id=pk)
    form1 = ListAuthor(instance=instance) #get the post object pk and fill the form

    if request.method == 'POST':
        form = ListAuthor(request.POST or None, request.FILES or None,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('app:home')
        else:
            print('123')
    context = {
        "form": form1,

    }

    return render(request, "app/post.html", context)

@login_required(login_url='app:login')
def addPost(request):

    form = ListAuthor()
    if request.method == "POST":
        form = ListAuthor(request.POST or None, request.FILES or None)
        if form.is_valid():
            Post = form.save()
            Post.save()
            return redirect('app:home')
    context = {'form': form}
    return render(request,'app/post.html',context)


def DeletePost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('app:home')
