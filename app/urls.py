from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app'
urlpatterns = [

    path('userpage/', views.postview, name='home'),  # change in here
    path('register/', views.register, name='register'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('post/', views.postview, name='post'),
    path('addPost/', views.addPost,name='addpost'),
    path('DeletePost/<int:pk>/', views.DeletePost, name='delete'),
    # path('updatepost/<int:pk>/', views.updatepost, name="update"),
    # path('userprofile/<int:pk>/', views.UserProfilePage, name="userprofile"),
    path('profile/', views.UserProfilePage, name='profile'),
    path('likepost/',views.likepost,name='likepost'),


]