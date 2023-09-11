from django.db import models
from django.contrib.auth.models import User
from .constants import Account_type,gender_type
# Create your models here.
class userBankAccountModel(models.Model):
    user=models.OneToOneField(User, related_name='account',on_delete=models.CASCADE)
    account_type=models.CharField(max_length=20,choices=Account_type)
    account_no=models.IntegerField(unique=True)
    birth_date=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=10,choices=gender_type)
    initial_deposit_date=models.DateTimeField(auto_now_add=True)
    balance=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    
    def __str__(self):
        return str(self.account_no)
    
class userAddressModel(models.Model):
    user=models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length= 100)
    street_address = models.CharField(default='ctg',max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.user.email