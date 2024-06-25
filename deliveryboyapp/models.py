from django.db import models
from adminapp.models import subcategory
from customerapp.models import checkout
from django.contrib.auth.models import User
# Create your models here.


class OrderProduct(models.Model):
    subcategory = models.ForeignKey(subcategory,on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    subtotal = models.FloatField()
    
class FinalBill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.FloatField()
    
class ConfirmOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    final = models.ForeignKey(FinalBill,on_delete=models.CASCADE)
    product = models.ForeignKey(subcategory,on_delete=models.CASCADE)
    quantity = models.FloatField()
    subtotal = models.FloatField()
    
    
class Billingaddress(models.Model):
    final = models.ForeignKey(FinalBill,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    email = models.EmailField(max_length=220)
    address = models.TextField(max_length=220)
    phone = models.BigIntegerField(max_length=220)
    other = models.CharField(max_length=220)
    client = models.ForeignKey(checkout,on_delete=models.CASCADE)