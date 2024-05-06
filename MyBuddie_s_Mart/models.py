from django.db import models
from django.contrib.auth.models import User
import os
import datetime


def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename ="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Shop(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    address =models.TextField(max_length=150,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at =models.DateTimeField(auto_now_add=True)
    map_location =models.TextField(max_length=500,null=True,blank=True)
    mobile = models.IntegerField(max_length=50,null=False,blank=False, default=0)
    telephone = models.IntegerField(max_length=50,null=False,blank=False, default=0)

    def __str__(self) :
        return self.name
    

class Product(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    product_image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    price =models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at =models.DateTimeField(auto_now_add=True)
    description = models.TextField( default="",max_length=250,null=False,blank=False)
    top_selling = models.BooleanField(default=False,help_text="0-show,1-hidden")
    current_price = models.FloatField(default=0,null=False,blank=False)
    offer =  models.IntegerField(default=0,null=False,blank=False)


    def __str__(self) :
        return self.name 

class Cart(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   shop_name=models.CharField(max_length=50,null=False,blank=False)
   product_name=models.CharField(default="", max_length=50,null=False,blank=False)
   product=models.ForeignKey(Product, on_delete=models.CASCADE)
   product_qty=models.IntegerField(null=False, blank=False)
   created_at=models.DateTimeField(auto_now_add=True)     

   @property
   def total_amount(self):
        return self.product_qty*self.product.price
