from django.contrib import admin
from django.urls import path
from Guest import views

app_name="webguest"

urlpatterns = [
    path('login/',views.login,name="login"), 
    path('',views.Home,name="Home"),
    path('newuser/',views.newuser_insert,name="newuser"),

]
    