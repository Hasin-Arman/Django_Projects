from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    price=models.IntegerField()
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class productReview(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,blank=True, null=True)
    reviewDate=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    review=models.CharField(max_length=300,default='')
    title=models.CharField(max_length=100,null=True, blank=True)
    