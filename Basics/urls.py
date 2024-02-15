from django.contrib import admin
from django.urls import path
from Basics import views

app_name="webbasics"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Calculator/',views.calculation,name="calculation"),
     path('home/',views.home,name="home"),

]