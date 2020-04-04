from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [

    path('',views.home.as_view(),name='home'),
    path('register/',views.register,name='register'),
    path('demo/',views.demo,name='demo'),
    path('login/',views.loginPage),
]