from django.urls import path
from customerapp import views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('acceptedrequest/',views.acceptedrequest,name='acceptedrequest'),
    path('shop/',views.shop,name='shop'),
    path('login/',views.login,name='login'),
    path('signin/',views.signin,name='signin'),
    path('about/',views.about,name='about'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('showdetails/<int:id>/',views.showdetails,name='showdetails'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('deliveryboy/',views.deliveryboy,name='deliveryboy'),
    path('myorder/',views.myorder,name='myorder'),
    
    
]