from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
# Create your views here.


def Homepage(request):
  if 'uid' in request.session:
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    return render(request,"User/Homepage.html",{'USER':userdata})
  else:
    return redirect('webguest:login')

def Myprofile(request):
  if 'uid' in request.session:
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    return render(request,"user/MyProfile.html",{'USER':userdata})
  else:
    return redirect('webguest:login')

def editprofile(request):
  if 'uid' in request.session:
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
      userdata.newuser_name=request.POST.get('txt_name')
      userdata.newuser_contact=request.POST.get('txt_contact')
      userdata.newuser_email=request.POST.get('txt_email')
      userdata.newuser_address=request.POST.get('txt_address')
      userdata.save()
      return render(request,"user/editprofile.html",{'USER':userdata})
  else: 
    return redirect('webguest:login')
        

def changepassword(request):
  if 'uid' in request.session:
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
      pwd=userdata.newuser_password
      currpwd=request.POST.get('txt_password')
      if pwd == currpwd:
        newpwd=request.POST.get('txt_newpassword')
        confpwd=request.POST.get('txt_confirmpassword')
        if newpwd == confpwd:
          userdata=tbl_newuser.objects.get(id=request.session["uid"])
          userdata.newuser_password=newpwd
          userdata.save()
        else:
          return render(request,"User/changepassword.html",{'msg':"Password Mismatch!!"}) 
      else:
        return render(request,"User/changepassword.html",{'msg':"Password Incorrect!!"}) 
  
    return render(request,"User/changepassword.html") 
  else: 
      return redirect('webguest:login')
 

def productsearch(request):
  if 'uid' in request.session:
    data=tbl_product.objects.all()
    if request.method=="POST":
      cat=request.POST.get('txtname')
      data=tbl_product.objects.filter(product_category=cat)
      return render(request,"User/productsearch.html",{'Data':data})
    else:
      return render(request,"User/productsearch.html",{'Data':data})
  else:
    return redirect('webguest:login')  

def employeesearch(request):
  if 'uid' in request.session:
    data=tbl_employee.objects.all()
    if request.method=="POST": 
      employee=request.POST.get('ddldept')
      data=tbl_employee.objects.filter(employee_dept=employee)
      return render(request,"User/employeesearch.html",{'data':data})
    else:
        return render(request,"User/employeesearch.html",{'data':data})
  else:
    return redirect('webguest:login')  
    



def complaint(request):
  if 'uid' in request.session:
    complaintdata=tbl_complaint.objects.all()
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
      tbl_complaint.objects.create(complaint_title=request.POST.get('txt_title'),complaint_content=request.POST.get("txt_content"),user=userdata)
      return render(request,"User/complaint.html",{'cdata':complaintdata})
    else:
      return render(request,"User/complaint.html",{'cdata':complaintdata})
  else: 
      return redirect('webguest:login')
   



    #----------Delete----------#


def delete_complaint(request,did):
 if 'uid' in request.session:
      tbl_complaint.objects.get(id=did).delete()
      return redirect('webuser:complaint')
 else: 
      return redirect('webguest:login')
   


def logout(request):
  if 'uid' in request.session:
   del request.session['uid']
   return redirect('webguest:login')
  else: 
         return redirect('webguest:login')
   


#-----Cart------

def Add_to_cart(request,pid):
  pdata=tbl_product.objects.get(id=pid)
  userdata=tbl_newuser.objects.get(id=request.session['uid'])
  bcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
  if bcount > 0:
    bdata=tbl_booking.objects.get(user=userdata,booking_status=0) 
    ccount=tbl_cart.objects.filter(booking=bdata,product=pdata).count()
    if ccount > 0:
      msg="Already added to cart"
      return render(request,"User/Homepage.html",{'msg':msg})
    else: 
      bookingid=tbl_booking.objects.get(id=bdata.id)
      productid=tbl_product.objects.get(id=pdata.id)
      tbl_cart.objects.create(booking=bookingid,product=productid)
      msg="Added to cart"
      return render(request,"User/Homepage.html",{'msg':msg})
  else:
    tbl_booking.objects.create(user=userdata)
      
  return render(request,"User/Homepage.html")

def cart(request):
  if 'uid' in request.session:
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    bookingdata=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingdata>0:
      booking=tbl_booking.objects.get(user=userdata,booking_status=0)
      cartdata=tbl_cart.objects.filter(booking=booking)
      return render(request,"User/cart.html",{'Data':cartdata})
    else:
      return render(request,"User/cart.html")
  else:
    return redirect('webuser:login')   


def checkout(request,cart):
  if 'uid' in request.session:
       userdata=tbl_newuser.objects.get(id=request.session["uid"])
       bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
       cartdata=tbl_cart.objects.filter(booking=bookingdata)
       bookingdata.booking_status=1
       bookingdata.save()
       return redirect("webuser:cart")
  else: 
      return redirect('webuser:login')
           