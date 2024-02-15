from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *


# Create your views here.


def login(request):
    if request.method=="POST":
            Email=request.POST.get('email')
            password=request.POST.get('password')
            print(Email,password)
            ulog=tbl_newuser.objects.filter(newuser_email=Email,newuser_password=password).count()
            print(ulog)
            alog=tbl_Admin.objects.filter(Admin_email=Email,Admin_password=password).count()
            if ulog > 0:
                userdata=tbl_newuser.objects.get(newuser_email=Email,newuser_password=password)
                request.session["uid"]=userdata.id
                request.session["uname"]=userdata.newuser_name
                return redirect('webuser:UserHome')
            

            elif alog > 0:
                Admindata=tbl_Admin.objects.get(Admin_email=Email,Admin_password=password)
                request.session["aid"]=Admindata.id
                request.session["aname"]=Admindata.Admin_name
                return redirect('webadmin:Home')

            else:

                return render(request,"Guest/login.html",{'msg':"Invalid Credentials!!"})
    else:
        return render(request,"Guest/login.html")
   

def Home(request):
    return render(request,"Guest/Home.html")


def newuser_insert(request):
    if 'aid' in request.session:
            newuserdata=tbl_newuser.objects.all()
            if request.method=="POST" and request.FILES:
                tbl_newuser.objects.create(newuser_name=request.POST.get("txtname"),newuser_contact=request.POST.get("txtcontact"),
                newuser_email=request.POST.get("txtemail"),newuser_address=request.POST.get("txtaddress"),newuser_photo=request.FILES.get("txtimage"),
                newuser_proof=request.FILES.get("txtproof"),newuser_password=request.POST.get("txtpassword"))
                return render(request,"Guest/newuser.html",{'newuser':newuserdata})
            else:
                return render(request,"Guest/newuser.html",{'newuser':newuserdata}) 
    else:
        return redirect('webguest:login')                   



