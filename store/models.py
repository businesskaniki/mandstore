from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=256,null=True)
    email = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name
class products(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.TextField(null=True)
    p_description = models.CharField(max_length=199)
    p_category = models.CharField(blank=True,null=True,max_length=100)
    p_image = models.ImageField(null = True, blank=True)

    def __str__(self):
        return self.p_name

class oder(models.Model):
    buyer = models.ForeignKey(customer,on_delete=models.CASCADE, null=True,blank=True)
    oderdate =models.DateField(auto_now=True)
    oderid = models.FloatField(null=True)

    def __str__(self):
        return self.buyer

class itemodered(models.Model):
    # odernmber=models.ForeignKey(oder,on_delete=models.CASCADE,null=True,blank=True)
    odereditem=models.ForeignKey(products,on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.CharField(max_length=100)
    def __str__(self):
        return self.quantity
class category(models.Model):
    product_category = models.CharField(max_length=100,null = True,)
    product_image = models.ImageField(max_length=100, null=True)
    product_descripton = models.CharField(max_length=100,null=True)