from django.db import models
from Admin.models import tbl_newuser,tbl_product

# Create your models here.

class tbl_booking(models.Model):
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    booking_status=models.IntegerField(default=0) 
    booking_date=models.DateField(auto_now=True)  


class tbl_cart(models.Model):
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    booking_quantity=models.IntegerField(default=1)
    


class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.TextField(max_length=50)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    complaint_date=models.DateField(auto_now=True) 
    complaint_replay=models.CharField(max_length=50,null=True)
  






