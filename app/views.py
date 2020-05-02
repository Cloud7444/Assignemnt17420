
from django.shortcuts import render, redirect ,HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from . form import UserRegisterForm ,ListAuthor,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from .models import Post, User,UserProfile
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView


def register(request):
    if request.user.is_authenticated:
        return redirect('app:home')
    else:
        form = UserRegisterForm()
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                UserProfile.objects.create(user=user)
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


@login_required(login_url='application:login')
def logoutpage(request):
    logout(request)
    return redirect('app:login')


@login_required(login_url='app:login')
def postview(request):
    allposts = Post.objects.all()

    context = {
        'allPost':allposts,
    }

    return render(request,'app/indexpage.html', context)

def likepost(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.is_liked= False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.is_liked = False
    else:
        post.likes.add(request.user)
        post.is_liked = True
    return redirect('app:home')

class userview(ListView):
    model = Post
    template_name = 'app/indexpage.html'
    context_object_name = 'allPost'
    ordering = ['-post_date']





# @login_required(login_url='app:login')
# def updatepost(request,pk):
#     instance = Post.objects.get(id=pk)
#     form1 = ListAuthor(instance=instance) #get the post object pk and fill the form
#
#     if request.method == 'POST':
#         form = ListAuthor(request.POST,instance=instance)
#         if form.is_valid():
#             # Post.author = request.user
#             form.save()
#             return redirect('app:home')
#         else:
#             print('123')
#     context = {
#         "form": form1,
#     }
#     return render(request, "app/post.html", context)

@login_required(login_url='app:login')
def addPost(request):
    form = ListAuthor()
    if request.method == "POST":
        form = ListAuthor(request.POST or None, request.FILES or None)
        if form.is_valid():
            Post = form.save()
            Post.author = request.user
            Post.save()
            return redirect('app:home')
    context = {'form': form}
    return render(request,'app/post.html',context)

@login_required(login_url='application:login')
def DeletePost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('app:profile')

@login_required(login_url='app:login')
def UserProfilePage(request,pk=None):
    # if pk:
    #     user = User.objects.get(pk=pk)
    #
    # else:
    #     user = request.user
    # userpost = request.user.post_set.all()
    # context ={'user':user,
    #           'post':userpost}
    # return render(request,'app/userprofile.html',context)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('app:profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    userpost = request.user.post_set.all()
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'post': userpost,

    }

    return render(request, 'app/userprofile.html', context)
