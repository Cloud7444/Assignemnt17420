
from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth import login, authenticate
from . form import UserRegisterForm ,ListAuthor
from django.contrib import messages
from django.views.generic import ListView
from .models import Post

class home(ListView):
    template_name = "app/indexpage.html"
    context_object_name = "POST"
    queryset = Post.objects.all()

def IndexHome(request):

    return render(request, 'app/indexpage.html')


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


#display the post
def postview(request):
    allposts = Post.objects.all()
    return render(request,'app/indexpage.html',
                  {'allPost' : allposts})


#the page to add post
def addPostPage(request):
    form = ListAuthor()
    context = {'form': form}
    return render(request,'app/post.html',context)




#function to add new post
def addPost(request):


    if request.method == "POST":
        form = ListAuthor(request.POST or None, request.FILES or None)
        if form.is_valid():
            Post = form.save()
            Post.save()
            return redirect('app:home')
        else:
            print('missing fileds')
    return redirect('app:home')

