from django.shortcuts import render,HttpResponse,redirect
from cart.cart import Cart
from customerapp import models
from adminapp import models as mo
from django.contrib.auth.models import User
from django.contrib import auth
from customerapp import forms   
from adminapp import forms as fooorm


# Create your views here.


#----------- LOGIN $ REGISTER--------------------------
def login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,
                          password=password)

        if user:
            auth.login(request,user)    
            return redirect(homepage)
        else:   
            return HttpResponse('LOGIN INVALID')
    
    return render(request,'customerapp/login.html')

def signin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    first_name= request.POST.get('first_name')
    if request.method =='POST':
        try:
            User.objects.get(username=username)
            return HttpResponse("username exists")
        except:
            user=User.objects.create_user(username=username,
                                         password=password,
                                         first_name=first_name)
    return render(request,'customerapp/login.html')

#-------- MY ORDERS-----------------------------
def acceptedrequest(request):
    # delivery = models.deliveryboy.objects.filter(user=request.user)
    # print(delivery)
    data = models.confirmbooking.objects.filter(user=request.user)
    print(data)
    return render(request,'customerapp/acceptedrequest.html',{'data':data})


#------------------HOME PAGE-----------------------------------------
def homepage(request):
    data=models.mo.subcategory.objects.all()[:3]
    
    return render(request,'customerapp/home.html',{'data':data})


#--------------RATELIST PAGE ---------------------------------------
def shop(request):
        data=models.mo.categories.objects.all()
        beta=models.mo.subcategory.objects.all()
       
        return render (request,'customerapp/shop.html',{'data':data,'beta':beta})


def showdetails(request,id):
    data=models.mo.categories.objects.all()
    beta=models.mo.subcategory.objects.filter(category=id)
    context = {'data':data,'beta':beta}
    return render(request,'customerapp/showdetails.html',context=context)

#------------------ ABOUT PAGE-----------------------------------------
def about(request):
    return render(request,'customerapp/about.html')

#-------------- REQUEST FOR PICKUP--------------------------------------------
def checkout(request):
    form= forms.checkoutform(request.POST)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.is_active = True
            obj.save()
            return redirect(thankyou)
        else:
            print(form.errors)
    return render(request,'customerapp/checkout.html')

#------------------ CONTACTUS PAGE----------------------------------------
def contact(request):
     form= forms.contactusform(request.POST)
     if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
        else:
            print(form.errors)
     return render(request,'customerapp/contact.html')

#-------------------- BE OUR DELIVERYBOY-------------------------------------------
def deliveryboy(request):
    form= fooorm.deliveryboyform(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect(homepage)
        else:
            print(form.errors)
    return render(request,"customerapp/deliveryboy.html")

#------------------ MY ORDER PAGE--------------------------------
def myorder(request):
    print(request.user)
    check = models.checkout.objects.get(email=request.user)
    data=models.confirmbooking.objects.filter(checkout_id=check)
    print(data)
    context = {'data':data}
    return render(request,"customerapp/myorder.html",context=context)

def thankyou(request):
    return render(request,'customerapp/thankyou.html')