from django.urls import path
from deliveryboyapp import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signin/',views.signin,name='signin'),
    path('shop/',views.shop,name='addshop'),
    path('cartview/',views.cartview,name='cartview'),
    path('request/',views.requestview,name='request'),
    path('acceptrequest/<int:id>/',views.acceptrequest,name='acceptrequest'),
    path('showdetails/<int:id>/',views.showdetails,name='showdetailss'),
    path('checkout/',views.checkoutview,name='checkouts'),
    path('checkout_view/',views.checkout_view,name='checkout_view'),
    path('rejectrequest/<int:id>/',views.rejectrequest,name='rejectrequest'),
    path('orderlist/',views.orderlist,name='orderlist'),
    
    path('bookscrap/',views.bookscrap,name='bookscrap'),

    
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
      
]
