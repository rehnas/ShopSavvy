from django.shortcuts import render

# Create your views here.
def calculation(request):
    if request.method=="POST":
        no1=int(request.POST.get('txtno1'))
        no2=int(request.POST.get('txtno2'))
        btn=request.POST.get('btnsubmit')
        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html")


def home(request):
    return render(request,"Basics/home.html")
