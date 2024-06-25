from django.shortcuts import render,HttpResponse,redirect
from adminapp.models import categories,coustomer,deliveryboy,subcategory
from deliveryboyapp import models
from customerapp import forms 
from customerapp.models import checkout,confirmbooking
from django.contrib import auth
from django.contrib.auth.models import User
from cart.cart import Cart
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from deliveryboyapp.forms import Billingform

import json

# Create your views here.


#------------------ LOGIN $ REGISTER---------------------------
from django.shortcuts import get_object_or_404
def login(request):
     if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,
                          password=password)

        if user:
            auth.login(request,user)  
           
            return redirect(requestview)
        else:   
            return HttpResponse('LOGIN INVALID')
     return render(request,'deliveryboyapp/login.html')
 
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
                                         first_name=first_name,
                                         is_staff = True)
    return render(request,'deliveryboyapp/login.html')


#---------------------SHOP----------------------------------
def shop(request):
        data=categories.objects.all()
        beta=subcategory.objects.all()
        return render(request,'deliveryboyapp/shop.html',{'data':data,'beta':beta})


#------------------- CART-----------------------------------------
def cartview(request):
    
    return render(request,'deliveryboyapp/cart.html')


def cart_add(request, id):
    cart = Cart(request)
    product = subcategory.objects.get(id=id)
    cart.add(product=product)
    return redirect(shop)


def item_clear(request, id):
    cart = Cart(request)
    product = subcategory.objects.get(id=id)
    cart.remove(product)
    return redirect(cartview)


def item_increment(request, id):
    cart = Cart(request)
    product = subcategory.objects.get(id=id)
    cart.add(product=product)
    return redirect(cartview)


def item_decrement(request, id):
    cart = Cart(request)
    product = subcategory.objects.get(id=id)
    cart.decrement(product=product)
    return redirect(cartview)


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(cartview)


def cart_detail(request):
    cart = Cart(request)
    request.cart[request.product.id] = {
                    'userid': request,
                    'product_id': request.product.id,
                    'name': request.product.name,
                  
    }
    print("ertyrtyhrt")
    print("fgdfgsfg".product_id)
    return render(request, 'cart/cart_detail.html')


#---------------------- REQUEST----------------------------------------------
def requestview(request):
    data = checkout.objects.filter(is_active=True)
    context = {'data':data}
    return render(request,'deliveryboyapp/request.html',context=context)

def acceptrequest(request,id):
    data = checkout.objects.get(id=id)
    delivery = deliveryboy.objects.get(user=request.user)
    print("dfgdhjh",delivery)
    form = forms.confirmbookingform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.checkout = data
            print(obj.checkout.name)
            obj.user = request.user
            obj.deliveryboy = delivery
            obj.save()
            data.is_active = False
            data.save()
            return redirect(shop)
        else:
            print(form.errors)
    return render(request,'deliveryboyapp/request.html')

def rejectrequest(request,id):
    data = checkout.objects.get(id=id)
    if request.method == "POST":
        data.is_reject = True
        data.save()
        
    return render(request,'deliveryboyapp/request.html')




def showdetails(request,id):
    data=categories.objects.all()
    beta=subcategory.objects.filter(category=id)
    context = {'data':data,'beta':beta}
    return render(request,'deliveryboyapp/showdetails.html',context=context)


#------------------ CHECKOUT-----------------------------------
def checkout_view(request):
    order = models.OrderProduct.objects.filter(user=request.user)
    final = models.FinalBill.objects.all()
    deli = deliveryboy.objects.get(email=request.user)
    data= confirmbooking.objects.filter(deliveryboy=deli)
    print("datattatataat",data)
    cart = Cart(request)
    subtotal = 0
    num = 0
    x = cart.cart.values()
    y = list(x)
    product_ids = [item['product_id'] for item in y]
    print(product_ids)


    for ab in cart.cart.values():
        pro = subcategory.objects.get(id=product_ids[num])
        subtotal += float(ab['price']) * float(ab['quantity'])
        sub = float(ab['price']) * float(ab['quantity'])
        num=num+1        
        
    gst = 0.18 * subtotal 
    total = subtotal - gst
    
   
 
    context = {'order':order,'final':final,'data':data,'subtotal':subtotal,'gst':gst,'total':total}
    return render(request,'deliveryboyapp/checkout.html',context=context)

def bookscrap(request):
    if request.method == "POST":
        cart = Cart(request)
        subtotal = 0
        num = 0
        x = cart.cart.values()
        y = list(x)
        product_ids = [item['product_id'] for item in y]
        print(product_ids)

        fnl = models.FinalBill.objects.create(user=request.user, total=0)

        for ab in cart.cart.values():
            pro = subcategory.objects.get(id=product_ids[num])
            subtotal += float(ab['price']) * float(ab['quantity'])
            sub = float(ab['price']) * float(ab['quantity'])
            order = models.ConfirmOrder.objects.create(user=request.user,
                                                    product=pro,
                                                    subtotal = sub,
                                                    quantity = ab['quantity'],
                                                    final = fnl)
            num=num+1        
            
        gst = 0.18 * subtotal 
        total = subtotal - gst
        
        fnl.total = total
        fnl.save()
        print("finallllllllll",fnl)
        
        form = Billingform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.final = fnl
            obj.save()
            chk = request.POST.get('client')
            check = confirmbooking.objects.get(checkout=chk)
            print("ggggggggggrrrrrrrrrr",check)
            check.is_ordered = True
            print("statussssssssss",check.is_ordered)
            check.save()            
            print("statussssssssss againnnn",check.is_ordered)
            
            cart.clear()
            print('gdddddddddddddd')
            return redirect(shop)
        else:
            print(form.errors)
    return render(request,'deliveryboyapp/checkout.html')


def checkoutview(request):
    products_json = request.POST.get('products')
    total_subtotal_str = request.POST.get('totalSubtotal')

    if products_json is None or total_subtotal_str is None:
        return JsonResponse({'error': 'Missing or invalid data in the request.'}, status=400)
    try:
        total_subtotal = float(total_subtotal_str)
    except ValueError:
        return JsonResponse({'error': 'Invalid totalSubtotal value.'}, status=400)

    gst = total_subtotal * 0.18
    final_total = total_subtotal - gst
    print(final_total)

    if not products_json:
        return JsonResponse({'error': 'No products data provided.'}, status=400)
    try:
        products = json.loads(products_json)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format in the products data.'}, status=400)

    for product in products:
        subcate = get_object_or_404(models.subcategory, name=product.get('name'))
        print("subcate", subcate)

        order_product = models.OrderProduct(
            subcategory=subcate,
            order_quantity=product.get('quantity', 0), 
            user=request.user,
            subtotal=product.get('subtotal', 0), 
        )
        print('save')
        order_product.save()

    final = models.FinalBill()
    final.order_prod = order_product 
    final.user = request.user
    final.save()
    print('datasave')
    return redirect(shop)




# import json
# def checkoutview(request):
#     products_json = request.POST.get('products')
#     products = json.loads(products_json)
#     total_subtotal = float(request.POST.get('totalSubtotal'))
#     gst = total_subtotal * 0.18
#     final_total = total_subtotal-gst
#     print(final_total)
#     for product in products:
#         subcate = models.subcategory.objects.filter(name=product['name'])
#         print("subcate",subcate)
#         order_product = models.OrderProduct(
#             subcategory=subcate,
#             order_quantity=product['quantity'],
#             user = request.user,
#             subtotal = total_subtotal,
#         )
#         order_product.save()
        
#     final = models.FinalBill()
#     final.order_prod = order_product
#     final.total = final_total
#     final.save()
#     return redirect(checkoutview)   




#------------- MY ORDER----------------------------------------------
def orderlist(request):
    deli = deliveryboy.objects.get(user=request.user)
    data  = confirmbooking.objects.filter(deliveryboy=deli).filter(is_ordered=False)
    print(data)
    context = {'data':data}
    return render(request,'deliveryboyapp/orderlist.html',context=context)