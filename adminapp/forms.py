from django import forms
from adminapp import models     
 
class categoryform(forms.ModelForm):
    class Meta:
        model=models.categories
        fields="__all__"

class subcategoryform(forms.ModelForm):
    class Meta:
        model=models.subcategory
        fields="__all__"
        
class deliveryboyform(forms.ModelForm):
    class Meta:
        model=models.deliveryboy
        fields="__all__"

class coustomerform(forms.ModelForm):
    class Meta:
        model=models.coustomer
        fields="__all__"