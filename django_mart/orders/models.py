from django.db import models
from django.contrib.auth.models import User
from store.models import Product
# Create your models here.

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)
    amount=models.FloatField()
    status=models.CharField(max_length=30)
    paid_at=models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_number=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    address_line1=models.CharField(max_length=100)
    address_line2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    order_note=models.TextField()
    order_total=models.IntegerField()
    tax=models.IntegerField()
    status=models.CharField(max_length=100,choices=STATUS,default='New')
    is_ordered=models.BooleanField(default=False)
    ordered_at=models.DateTimeField(auto_now_add=True)
    ip=models.CharField(max_length=100,blank=True,null=True)
    
class OrderedProduct(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
    
class PaymentGateWaySettings(models.Model):
    store_id=models.CharField(max_length=500,null=True, blank=True)
    store_pass=models.CharField(max_length=500,null=True, blank=True)