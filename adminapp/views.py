from django.shortcuts import render,HttpResponse,redirect
from adminapp import models
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import auth
from adminapp import forms
from customerapp import models as mo
from adminapp import forms
from customerapp.models import confirmbooking
from deliveryboyapp.models import FinalBill,Billingaddress,ConfirmOrder
import random 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



#--------------LOGIN $ REGISTER $ LOGOUT ------------------------------------------------

def login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,
                          password=password)
        print(user)
        if user:
            auth.login(request,user)    
            return redirect(adminhomepage)
        else:   
            return HttpResponse('LOGIN INVALID')
    return render(request,'login.html')

def register(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method =='POST':
        try:
            User.objects.get(username=username)
            return HttpResponse("username exists")
        except:
            user=User.objects.create_user(username=username,
                                         password=password,
                                         is_superuser = True)
            return redirect(login)
    
    return render(request,'register.html')

def logoutview(request):
    logout(request)
    return redirect(login)
#-------HOME PAGE---------------------------------------

def homepage(request):
    if request.user.is_superuser:
        return render(request,'home.html')
    else:
        return redirect(login)

def adminhomepage(request):
    return render(request,'adminhomepage.html')

#-------------------------- CATEGORIES------------------------------------
def addcategories(request):
    form= forms.categoryform(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(showcategories)
        else:
            print(form.errors)
            
    return render(request,'addcategories.html')

def showcategories(request):
    data= models.categories.objects.all()
    context = {'data':data} 
    return render(request,'showcategories.html', context=context)

def deleteview(request,id):
    data= models.categories.objects.get(id=id)
    data.delete()
    return redirect(showcategories)

def editview(request,id):
    data=models.categories.objects.get(id=id)
    context={'data':data}
    return render(request,'editcategories.html',context=context)

def updateview(request,id):
    data = models.categories.objects.get(id=id)
    form = forms.categoryform(request.POST,instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(showcategories)
        else:
            print(form.errors)
    return render(request,'editcategories.html')    

def add_deliveryboy(request):
    form= forms.deliveryboyform(request.POST,request.FILES)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()  
            return redirect(managedeliveryboy)
        else:
            print(form.errors)
            
    return render(request,'adddeliveryboy.html')

def managedeliveryboy(request):
    data=models.deliveryboy.objects.all()
    context={'data':data}
    return render(request,'managedeliveryboy.html',context=context)

#---------------- DELIVERYBOY---------------------------------------------
def editdeliveryboy(request,id):
    data=models.deliveryboy.objects.get(id=id)
    context={'data':data}
    return render(request,'editdeliveryboy.html',context=context)

def deletedeliveryboy(request,id):
    data= models.deliveryboy.objects.get(id=id)
    data.delete()
    return redirect(managedeliveryboy)


def updatedelivery(request,id):
    data = models.deliveryboy.objects.get(id=id)
    form = forms.deliveryboyform(request.POST,instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(managedeliveryboy)
        else:
            print(form.errors)
    return render(request,'editdeliveryboy.html')    

def requestdeliveryboy(request):
    data= models.deliveryboy.objects.filter(is_registered=False)
    context = {'data':data} 
    return render(request,'requestdeliveryboy.html', context=context)

def acceptdeliveryboy(request,id):
    data = models.deliveryboy.objects.get(id=id)
    emaill = data.email
    code = random.randint(100000,999999)
    print("bfdksjf",code)
    code = str(code)
    deli = User.objects.create_user(username=emaill ,password=code,email=data.email)
    print("dfgre",deli)
    data.is_registered = True
    data.save()
    try:
        subject = "Forgot Password"
        msg = f"Your Login Id and password for deliveryboy in scarify is : '{data.email}' is {code}."
        from_email = settings.EMAIL_HOST_USER
        receipent = [emaill]
        send_mail(subject, msg, from_email, receipent)
        print("mail send...................")
    except Exception as e:
        print("errorrrr",e)
    return redirect(requestdeliveryboy)


#--------------------CUSTOMER-----------------------------------------------------

def addcoustomer(request):
   form=forms.coustomerform(request.POST)
   if request.method=="POST":
     if form.is_valid():
        form.save()
        return redirect(adminhomepage)
     else:
            print(form.errors)        
   return render(request,'addcoustomer.html')

def managecustomer(request):
    data=User.objects.filter(is_superuser=False).filter(is_staff=False)
    context={'data':data}
    return render(request,'managecustomer.html',context=context)

def deletecustomer(request,id):
    data= models.coustomer.objects.get(id=id)
    data.delete()
    return redirect(managecustomer)

# ---------------------------------------- Sub category -------------------------------------------------------------

def addsubcategory(request):
    data = models.categories.objects.all()
    form = forms.subcategoryform(request.POST,request.FILES)
    if request.method=="POST":
     if form.is_valid():
        form.save()
        return redirect(showsubcategory )
     else:
            print(form.errors)  
    context ={'data':data}
    return render(request,'addsubcategory.html',context=context)

def showsubcategory(request):
    data= models.subcategory.objects.all()
    context = {'data':data} 
    return render(request,'showsubcategory.html',context=context)

def deletesubcategory(request,id):
    data= models.subcategory.objects.get(id=id)
    data.delete()
    return redirect(showsubcategory)

#----------------------------------FEEDBACK------------------------------------
def managefeedback(request):
    data = mo.contactus.objects.all()
    context={'data':data}
    return render(request,'managefeeback.html',context=context)

def deletefeedback(request,id):
    data=  mo.contactus.objects.get(id=id)
    data.delete()
    return redirect(managefeedback)  
 
 
 
#------------------------------ SCRAPPER-------------------------------------------
def pickupview(request):
    # data = FinalBill.objects.all()
    conf = Billingaddress.objects.all()
    return render(request,'pickupconfirm.html',{'data':conf})



def ViewDetails(request,id):
    conf = Billingaddress.objects.get(id=id)
    conf_order = ConfirmOrder.objects.filter(final=conf.final)
    final = FinalBill.objects.get(id=conf.final.id)
    print("finallll",final)
    print(conf_order)
    context = {'final':final,'conf_order':conf_order}
    return render(request,'ViewDetails.html',context)