from django.contrib import admin
from django.urls import path
from User import views

app_name="webuser"

urlpatterns = [
    path('userhome/',views.Homepage,name="UserHome"),
    path('MyProfile/',views.Myprofile,name="MyProfile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('productsearch/',views.productsearch,name="productsearch"),
    path('employeesearch/',views.employeesearch,name="employeesearch"),
    path('complaint/',views.complaint,name="complaint"), 
    path('delete_complaint/<int:did>',views.delete_complaint,name="delete_complaint"),
    path('logout/',views.logout,name="logout"),
    path('Add_to_cart/<int:pid>',views.Add_to_cart,name="Add_to_cart"),
    path('cart',views.cart,name="cart"),
    path('checkout/<int:cart>',views.checkout,name="checkout")
      


]