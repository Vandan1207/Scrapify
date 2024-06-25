from django import forms 
from deliveryboyapp import models

class Billingform(forms.ModelForm):
    class Meta:
        model = models.Billingaddress
        fields = "__all__"
        exclude = ('user','final')