from django.db import models

# Create your models here.


class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
        

class tbl_Brand(models.Model):
    Brand_name=models.CharField(max_length=50)

class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=50,null=True)
    employee_gender=models.CharField(max_length=50)
    employee_dept=models.CharField(max_length=50)
    employee_salary=models.CharField(max_length=50)

class tbl_Admin(models.Model):
    Admin_name=models.CharField(max_length=50)
    Admin_contact=models.CharField(max_length=50)
    Admin_email=models.CharField(max_length=50)
    Admin_password=models.CharField(max_length=50)    



class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.SET_NULL,null=True)

class tbl_subdistrict(models.Model):
    subdistrict_name=models.CharField(max_length=50)    
    district=models.ForeignKey(tbl_district,on_delete=models.SET_NULL,null=True)


class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    place_pincode=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.SET_NULL,null=True)

class tbl_product(models.Model):
    item_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_category=models.CharField(max_length=50,null=True)
    product_details=models.CharField(max_length=50)
    product_image=models.FileField(upload_to="product_imgs/",null=True)

class tbl_newuser(models.Model):
    newuser_name=models.CharField(max_length=50)
    newuser_contact=models.CharField(max_length=50)
    newuser_email=models.CharField(max_length=50)
    newuser_address=models.CharField(max_length=50)
    newuser_photo=models.FileField(upload_to="newuser_imgs/")
    newuser_proof=models.FileField(upload_to="newuser_imgs/")
    newuser_password=models.CharField(max_length=50)
    

class tbl_item(models.Model):
    item_itemcode=models.CharField(max_length=50)
    item_itemname=models.CharField(max_length=50)
    item_price=models.CharField(max_length=50)
    item_description=models.CharField(max_length=50)
    item_image=models.FileField(upload_to="item_imgs/")




      

    
    
    
    
    
    
    
    
    
    
    