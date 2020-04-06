from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [

    path('',views.postview,name='home'),
    path('register/',views.register,name='register'),
    path('demo/',views.demo,name='demo'),
    path('login/',views.loginPage),
    path('post/',views.postview,name='post'),
    path('addPostPage/',views.addPostPage),
    path('addPost/',views.addPost),
]