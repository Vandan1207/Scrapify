from django.urls import path
from adminapp import views
urlpatterns = [
    
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('homepage/',views.homepage,name='homepage'),
    path('adminhomepage/',views.adminhomepage,name='adminhomepage'),
    path('addcategories/',views.addcategories,name='addcategories'),
    path('showcategories/',views.showcategories,name='showcategories'),
    path('deleteview/<int:id>/',views.deleteview,name='deleteview'),
    path('editview/<int:id>/',views.editview,name='editview'),
    path('updateview/<int:id>/',views.updateview,name='updateview'),
    path('add_deliveryboy/',views.add_deliveryboy,name='add_deliveryboy'),
    path('managedeliveryboy/',views.managedeliveryboy,name='managedeliveryboy'),
    path('editdeliveryboy/<int:id>/',views.editdeliveryboy,name='editdeliveryboy'),
    path('deletedeliveryboy/<int:id>/',views.deletedeliveryboy,name='deletedeliveryboy'),
    path('updatedelivery/<int:id>/',views.updatedelivery,name='updatedelivery'),
    path('logout/',views.logoutview,name='logout'),
    path('addcoustomer/',views.addcoustomer,name='addcoustomer'),
    path('managecustomer/',views.managecustomer,name='managecustomer'),
    path('deletecustomer/<int:id>/',views.deletecustomer,name='deletecustomer'),
    path('showsubcategory/',views.showsubcategory,name='showsubcategory'),
    path('deletesubcategory/<int:id>/',views.deletesubcategory,name='deletesubcategory'),
    path('addsubcategory/',views.addsubcategory,name='addsubcategory'),
    path('managefeedback/',views.managefeedback,name='managefeedback'),
    path('deletefeedback/<int:id>/',views.deletefeedback,name='deletefeedback'),
    path('pickupview/',views.pickupview,name='pickupview'),
    path('requestdeliveryboy/',views.requestdeliveryboy,name='requestdeliveryboy'),
    path('ViewDetails/<int:id>/',views.ViewDetails,name='ViewDetails'),
    
    path('acceptdeliveryboy/<int:id>/',views.acceptdeliveryboy,name='acceptdeliveryboy'),
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
]
