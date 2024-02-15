from django.contrib import admin
from django.urls import path
from Admin import views

app_name="webadmin"

urlpatterns = [

    path('home/',views.home,name="Home"),
    
    path('district/',views.district_insert,name="district"),
    path('category/',views.category_insert,name="category"),
    path('Brand/',views.Brand_insert,name="Brand"),
    path('employee/',views.employee_insert,name="employee"),
    path('AdminReg/',views.Admin_insert,name="AdminReg"),
    path('subcategory/',views.subcategory_insert,name="subcategory"),
    path('place/',views.place_insert,name="place"),
    path('product/',views.product_insert,name="product"),
    path('subdistrict/',views.subdistrict_insert,name="subdistrict"),
    path('newuser/',views.newuser_insert,name="newuser"),
    path('item/',views.item_insert,name="item"),
    path('user_complaint/',views.user_complaints,name="usercomplaint"),


    path('delete_district/<int:did>',views.delete_district,name="delete_district"),
    path('delete_category/<int:did>',views.delete_category,name="delete_category"),
    path('delete_Brand/<int:did>',views.delete_Brand,name="delete_Brand"),
    path('delete_employee/<int:did>',views.delete_employee,name="delete_employee"),
    path('delete_Admin/<int:did>',views.delete_Admin,name="delete_admin"),
    path('delete_subcategory/<int:did>',views.delete_subcategory,name="delete_subcategory"),
    path('delete_product/<int:did>',views.delete_product,name="delete_product"),
    path('delete_subdistrict/<int:did>',views.delete_subdistrict,name="delete_subdistrict"),
    path('delete_newuser/<int:did>',views.delete_newuser,name="delete_newuser"),
    path('delete_item/<int:did>',views.delete_item,name="delete_item"),


    
    path('edit_district/<int:eid>',views.edit_district,name="edit_district"),
    path('edit_category/<int:eid>',views.edit_category,name="edit_category"),
    path('edit_brand/<int:eid>',views.edit_brand,name="edit_brand"),
    path('edit_Admin/<int:eid>',views.edit_Admin,name="edit_Admin"),
    path('edit_subcategory/<int:eid>',views.edit_subcategory,name="edit_subcategory"),
    path('edit_place/<int:eid>',views.edit_place,name="edit_place"),
    path('edit_product/<int:eid>',views.edit_product,name="edit_product"),
    path('edit_subdistrict/<int:eid>',views.edit_subdistrict,name="edit_subdistrict"),
    path('edit_newuser/<int:eid>',views.edit_newuser,name="edit_newuser"),
    path('edit_item/<int:eid>',views.edit_item,name="edit_item"),
   
   path('replay_user_complaint/<int:eid>',views.replay_user_complaint,name="Replay"),

    
]
    