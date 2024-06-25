from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class categories(models.Model):
    name=models.CharField(max_length=255)
    
class subcategory(models.Model):
    category = models.ForeignKey(categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='sub_images')
    
class deliveryboy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    address=models.TextField()
    phonenumber=models.BigIntegerField()
    adharnumber=models.ImageField(upload_to='deliveryboyadharcard/',null=True,blank=True)
    image = models.ImageField(upload_to='deliveryboyimg/',null=True,blank=True)
    is_registered = models.BooleanField(default=False)
    
class coustomer(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    city=models.TextField()
    phonenumber=models.BigIntegerField()
    