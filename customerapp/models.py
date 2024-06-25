from django.db import models
from adminapp import models as mo
from django.contrib.auth.models import User
from adminapp.models import deliveryboy

class checkout(models.Model):
    name=models.TextField()
    email=models.EmailField(max_length=255)
    phone=models.BigIntegerField()
    city=models.TextField()
    address=models.CharField(max_length=500)
    approxweight=models.BigIntegerField()
    timeslot=models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_reject = models.BooleanField(default=False)

class contactus(models.Model):
    name=models.TextField(max_length=255)
    email=models.EmailField()
    phone=models.BigIntegerField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)

class confirmbooking(models.Model):
    checkout = models.ForeignKey(checkout,on_delete=models.CASCADE)
    deliveryboy = models.ForeignKey(deliveryboy,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_ordered = models.BooleanField(default=False)
    