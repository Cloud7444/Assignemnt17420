from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [

    path('',views.postview,name='home'), #change in here
    path('user/',views.userpage,name='userpage'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('post/',views.postview,name='post'),
    path('addPost/',views.addPost),
    path('DeletePost/<int:pk>/',views.DeletePost,name='delete'),
    path('updatepost/<int:pk>/',views.updatepost,name="update"),

]