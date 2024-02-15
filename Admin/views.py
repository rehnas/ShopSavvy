from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
# Create your views here.


def district_insert(request):
    if 'aid' in request.session:
            districtdata=tbl_district.objects.all()
            if request.method=="POST":
                tbl_district.objects.create(district_name=request.POST.get('txtname'))
                return render(request,"Admin/District.html",{'district':districtdata})
            else:
                return render(request,"Admin/District.html",{'district':districtdata})
    else:
      return redirect('webadmin:login')

def category_insert(request):
    if 'aid' in request.session:
        categorydata=tbl_category.objects.all()
        if request.method=="POST":
            tbl_category.objects.create(category_name=request.POST.get('txtname'))
            return render(request,"Admin/category.html",{'category':categorydata})
        else:
            return render(request,"Admin/category.html",{'category':categorydata})
    else:
        return redirect('webadmin:login')

def Brand_insert(request):
    if 'aid' in request.session:
        Branddata=tbl_Brand.objects.all()
        if request.method=="POST":
            tbl_Brand.objects.create(Brand_name=request.POST.get('txtname'))
            return render(request,"Admin/brand.html",{'Brand':Branddata})
        else:
            return render(request,"Admin/brand.html",{'Brand':Branddata})
    else:
        return redirect('webadmin:login')



def employee_insert(request):
    if 'aid' in request.session:
        employeedata=tbl_employee.objects.all()
        if request.method=="POST":
            tbl_employee.objects.create(employee_name=request.POST.get("txtname"),employee_gender=request.POST.get("gender"),employee_dept=request.POST.get("ddldept"),employee_salary=request.POST.get("txtno"))
            return render(request,"Admin/employee.html",{'employee':employeedata})
        else:
            return render(request,"Admin/employee.html",{'employee':employeedata})
    else:
        return redirect('webadmin:login')       

def Admin_insert(request):
    if 'aid' in request.session:
        Admindata=tbl_Admin.objects.all()
        if request.method=="POST":
            tbl_Admin.objects.create(Admin_name=request.POST.get("txtname"),Admin_contact=request.POST.get("txtnum"),Admin_email=request.POST.get("txtemail"),Admin_password=request.POST.get("txtpassword"))
            return render(request,"Admin/Admin.html",{'Admin':Admindata})
        else:
            return render(request,"Admin/Admin.html",{'Admin':Admindata})
    else:
        return redirect('webadmin:login')



def subcategory_insert(request):
    if 'aid' in request.session:
        categorydata=tbl_category.objects.all()
        subcategorydata=tbl_subcategory.objects.all()
        if request.method=="POST":

            catid=tbl_category.objects.get(id=request.POST.get('sel_cat'))

            tbl_subcategory.objects.create(subcategory_name=request.POST.get('txt_subcat'),category=catid)
            return render(request,"Admin/Subcategory.html",{'catdata':categorydata,'subcategory':subcategorydata})
        else:
            return render(request,"Admin/Subcategory.html",{'catdata':categorydata,'subcategory':subcategorydata})
    else:
        return redirect('webadmin:login')

def subdistrict_insert(request):
    if 'aid' in request.session:
        districtdata=tbl_district.objects.all()
        subdistrictdata=tbl_subdistrict.objects.all()
        if request.method=="POST":

            disid=tbl_district.objects.get(id=request.POST.get('sel_dis'))

            tbl_subdistrict.objects.create(subdistrict_name=request.POST.get('txt_subdis'),district=disid)
            return render(request,"Admin/Subdistrict.html",{'disdata':districtdata,'subdistrict':subdistrictdata})
        else:
            return render(request,"Admin/Subdistrict.html",{'disdata':districtdata,'subdistrict':subdistrictdata})    
    else:
        return redirect('webadmin:login')


def place_insert(request):
    if 'aid' in request.session:
        districtdata=tbl_district.objects.all()
        if request.method=="POST":

            disid=tbl_district.objects.get(id=request.POST.get('sel_dis'))
            tbl_place.objects.create(place_name=request.POST.get('txt_place'),place_pincode=request.POST.get('txt_pincode'),district=disid)
            return render(request,"Admin/place.html",{'disdata':districtdata})
        else:
            return render(request,"Admin/place.html",{'disdata':districtdata})   
    else:
        return redirect('webadmin:login')

def product_insert(request):
    if 'aid' in request.session:
        productdata=tbl_product.objects.all()
        if request.method=="POST" and request.FILES:
            tbl_product.objects.create(item_name=request.POST.get("item name"),
            product_price=request.POST.get("price"),
            product_category=request.POST.get("category"),
            product_details=request.POST.get("details"),
            product_image=request.FILES.get("txtimage"))
            return render(request,"Admin/product.html",{'product':productdata})
        else:
            return render(request,"Admin/product.html",{'product':productdata})
    else:
        return redirect('webadmin:login')        

def newuser_insert(request):
    if 'aid' in request.session:
            newuserdata=tbl_newuser.objects.all()
            if request.method=="POST" and request.FILES:
                tbl_newuser.objects.create(newuser_name=request.POST.get("txtname"),newuser_contact=request.POST.get("txtcontact"),
                newuser_email=request.POST.get("txtemail"),newuser_address=request.POST.get("txtaddress"),newuser_photo=request.FILES.get("txtimage"),
                newuser_proof=request.FILES.get("txtproof"),newuser_password=request.POST.get("txtpassword"))
                return render(request,"Admin/newuser.html",{'newuser':newuserdata})
            else:
                return render(request,"Admin/newuser.html",{'newuser':newuserdata}) 
    else:
        return redirect('webadmin:login')                   


def item_insert(request):
    if 'aid' in request.session:
        itemdata=tbl_item.objects.all()
        if request.method=="POST" and request.FILES:
            tbl_item.objects.create(item_itemcode=request.POST.get("itemcode"),item_itemname=request.POST.get("itemname"),
            item_price=request.POST.get("price"),item_description=request.POST.get("description"),item_image=request.FILES.get("txtimage"))
            return render(request,"Admin/item.html",{'item':itemdata})
        else:
            return render(request,"Admin/item.html",{'item':itemdata})    
    else:
         return redirect('webadmin:login')


def home(request):
    if 'aid' in request.session:
       return render(request,"Admin/Home.html")
    else:
        return redirect('webadmin:login')




def user_complaints(request):
    if 'aid' in request.session:
        complaintdata=tbl_complaint.objects.all()
        return render(request,"Admin/user_complaint.html",{'Ucomplaint': complaintdata})
    else:
        return redirect('webadmin:login')




def replay_user_complaint(request,eid):
    if 'aid' in request.session:
        cmpdata=tbl_complaint.objects.get(id=eid)
        if request.method=="POST":
            cmpdata.complaint_replay=request.POST.get('txt_reply')
            cmpdata.complaint_status=1
            cmpdata.save()
            return redirect('webadmin:usercomplaint')
        else:
            return render(request,"Admin/replay.html")
    else:
        return redirect('webadmin:login')









#----------Delete----------#


def delete_district(request,did):
    if 'aid' in request.session:
        tbl_district.objects.get(id=did).delete()
        return redirect('webadmin:district')
    else:
        return redirect('webadmin:login')


def delete_category(request,did):
    if 'aid' in request.session:
        tbl_category.objects.get(id=did).delete()
        return redirect('webadmin:category')
    else:
        return redirect('webadmin:login')
   


def delete_Brand(request,did):
    if 'aid' in request.session:
        tbl_Brand.objects.get(id=did).delete()
        return redirect('webadmin:Brand')
    else:
        return redirect('webadmin:login')

 
def delete_employee(request,did):
    if 'aid' in request.session:
        tbl_employee.objects.get(id=did).delete()
        return redirect('webadmin:employee')
    else:
        return redirect('webadmin:login')


def delete_Admin(request,did):
    if 'aid' in request.session:
        tbl_Admin.objects.get(id=did).delete()
        return redirect('webadmin:Admin')  
    else:
        return redirect('webadmin:login')


def delete_subcategory(request,did):
    if 'aid' in request.session:
        tbl_subcategory.objects.get(id=did).delete()
        return redirect('webadmin:subcategory') 
    else:
        return redirect('webadmin:login')
  


def delete_place(request,did):
    if 'aid' in request.session:
        tbl_place.objects.get(id=did).delete()
        return redirect('webadmin:place') 
    else:
        return redirect('webadmin:login')
 

def delete_product(request,did):
    if 'aid' in request.session:
        tbl_product.objects.get(id=did).delete()
        return redirect('webadmin:product') 
    else:
        return redirect('webadmin:login')
   


def delete_subdistrict(request,did):
    if 'aid' in request.session:
        tbl_subdistrict.objects.get(id=did).delete()
        return redirect('webadmin:subdistrict')    
    else:
        return redirect('webadmin:login')


def delete_newuser(request,did):
    if 'aid' in request.session:
        tbl_newuser.objects.get(id=did).delete()
        return redirect('webadmin:newuser')  
    else:
        return redirect('webadmin:login')


def delete_item(request,did):
    if 'aid' in request.session:
        tbl_item.objects.get(id=did).delete()
        return redirect('webadmin:item') 
    else:
        return redirect('webadmin:login')
        



#-----------Edit------------#


def edit_district(request,eid):
    if 'aid' in request.session:
        distdata=tbl_district.objects.get(id=eid)
        districtdata=tbl_district.objects.all()
        if request.method=="POST":
            distdata.district_name=request.POST.get('txtname')
            distdata.save()
            return redirect('webadmin:district')
        else:
            return render(request,"Admin/District.html",{'DIS':distdata,'district':districtdata})

    else:
        return redirect('webadmin:login')



def edit_category(request,eid):
    if 'aid' in request.session:
        category1data=tbl_category.objects.get(id=eid) 
        categorydata=tbl_category.objects.all()
        if request.method=="POST":
            category1data.category_name=request.POST.get("txtname")   
            category1data.save()
            return redirect('webadmin:category')
        else:
            return render(request,"Admin/category.html",{'category':category1data,'category':categorydata})       
    else:
        return redirect('webadmin:login')



def edit_brand(request,eid):
    if 'aid' in request.session:
        brand1data=tbl_Brand.objects.get(id=eid)
        branddata=tbl_Brand.objects.all()
        if request.method=="POST":
            brand1data.Brand_name=request.POST.get("txtname")
            brand1data.save()
            return redirect('webadmin:Brand')
        else:
             return render(request,"Admin/brand.html",{'branddata':brand1data,'Brand':branddata})
    else:
        return redirect('webadmin:login')
    

def edit_Admin(request,eid):
    if 'aid' in request.session:
        Admin1data=tbl_Admin.objects.get(id=eid)
        Admindata=tbl_Admin.objects.all()
        if request.method=="POST":
            Admin1data.Admin_name=request.POST.get("txtname")
            Admin1data.Admin_contact=request.POST.get("txtnum")
            Admin1data.Admin_email=request.POST.get("txtemail")
            Admin1data.Admin_password=request.POST.get("txtpassword")
            Admin1data.save()
            return redirect('webadmin:Admin')
        else:
                return render(request,"Admin/Admin.html",{'Admindata':Admin1data,'Admin':Admindata})
    else:
        return redirect('webadmin:login')


def edit_subcategory(request,eid):
    if 'aid' in request.session:
        subcategory1data=tbl_subcategory.objects.get(id=eid)  
        subcategorydata=tbl_subcategory.objects.all()
        categorydata=tbl_category.objects.all()
        if request.method=="POST":
            categ=request.POST.get('sel_cat')
            subcategory1data.category=tbl_category.objects.get(id=categ)
            subcategory1data.subcategory_name=request.POST.get("txt_subcat")
            subcategory1data.save()
            return redirect('webadmin:subcategory')
        else:
            return render(request,"Admin/Subcategory.html",{'catdata':categorydata,'Subdata':subcategory1data,'subcategory':subcategorydata})   
    else:
        return redirect('webadmin:login')   



def edit_subdistrict(request,eid):
    if 'aid' in request.session:
        subdistrict1data=tbl_subdistrict.objects.get(id=eid)
        subcategorydata=tbl_subdistrict.objects.all()
        districtdata=tbl_district.objects.all()
        if request.method=="POST":
            dist=request.POST.get('sel_dis')
            subdistrict1data.district=tbl_district.objects.get(id=dist)
            subdistrict1data.subdistrict_name=request.POST.get("txt_subdis")    
            subdistrict1data.save()
            return redirect('webadmin:subdistrict') 
        else:
            return render(request,"Admin/subdistrict.html",{'disdata':districtdata,'disdata':subdistrict1data,'subdistrict':subdistrictdata})    
    else:
        return redirect('webadmin:login')    


def edit_place(request,eid):
    if 'aid' in request.session:
        place1data=tbl_place.get(id=eid)
        placedata=tbl_place.objects.all()
        if request.method=="POST":
            dis=request.POST.get('sel_dis')
            place1data.district=tbl_district.objects.get(id=dis)
            place1data.place_name=request.POST.get("txt_place")
            place1data.place_pincode=request.POST.get("txt_pincode")
            place1data.save()
            return redirect('webadmin:place')
        else:
            return render(request,"Admin/place.html",{'disdata':districtdata,'placedata':place1data,'place':placedata})  
    else:
        return redirect('webadmin:login')          


def edit_product(request,eid):
    if 'aid' in request.session:
        product1data=tbl_product.get(id=eid)   
        productdata=tbl_product.objects.all()
        if request.method=="POST":
            product1data.item_name=request.POST.get("item_name")  
            product1data.product_price=request.POST.get("price")
            product1data.product_category=request.POST.get("category")
            product1data.product_details=request.POST.get("details")
            product1data.save()
            return redirect('webadmin:product')
        else:
            return render(request,"Admin/product.html",{'product':product1data,'product':productdata})   
    else:
        return redirect('webadmin:login') 


def edit_newuser(request,eid):
    if 'aid' in request.session:
        newuser1data=tbl_newuser.get(id=eid)
        newuser=tbl_newuser.objects.all()
        if request.method=="POST":
            newuser1data.newuser_name=request.POST.get("txtname")
            newuser1data.newuser_contact+request.POST.get("txtcontact")  
            newuser1data.newuser_email=request.POST.get("txtemail") 
            newuser1data.newuser_address=request.POST.get("txtaddress")
            newuser1data.newuser_photo=request.FILES.get("txtimage")
            newuser1data.newuser_proof=request.FILES.get("txtproof")
            newuser1data.newuser_password=request.POST.get("txtpassword")
            newuser1data.newuser_confirmpassword=request.POST.get("txtconfirmpassword")
            newuser1data.save()
            return redirect('webadmin:newuser')
        else:
                return render(request,"Admin/newuser.html",{'newuser':newuser1data,'newuser':newuserdata})
    else:
        return redirect('webadmin:login')            



def edit_item(request,eid):
    if 'aid' in request.session:
        item1data=tbl_item.get(id=eid)   
        itemdata=tbl_item.objects.all()
        if request.method=="POST":
            item1data.item_code=request.POST.get("item_code")  
            item1data.item_name=request.POST.get("item_name")
            item1data.item_price=request.POST.get("price")
            item1data.item_description=request.POST.get("description")
            item1data.item_photo=request.FILES.get("txtimage")
            item1data.save()
            return redirect('webadmin:item')
        else:
            return render(request,"Admin/item.html",{'item':item1data,'item':itemdata})          
    else:
        return redirect('webadmin:login')        





















