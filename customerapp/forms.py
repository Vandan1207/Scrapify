from django import forms
from customerapp import models     

class checkoutform(forms.ModelForm):
    class Meta:
        model =models.checkout
        fields="__all__"
        
class contactusform(forms.ModelForm):
    class Meta:
        model =models.contactus
        fields="__all__"
        
        
class confirmbookingform(forms.ModelForm):
    class Meta:
        model =models.confirmbooking
        fields="__all__"
        exclude = ('checkout','user','deliveryboy',)