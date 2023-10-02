from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ACCOUNT_TYPE=(
    ('Savings','Savings'),
    ('Current','Current'),
)

GENDER_TYPE=(
    ('Male','Male'),
    ('Female','Female'),
)
class userBankAccount(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    account_type=models.CharField(max_length=20,choices=ACCOUNT_TYPE)
    gender=models.CharField(max_length=20,choices=GENDER_TYPE)
    birth_date=models.DateField(null=True, blank=True)
    account_no=models.IntegerField(unique=True)
    initial_deposit=models.DateTimeField(auto_now_add=True)
    balance=models.DecimalField(max_digits=10,default=0, decimal_places=2)
    
    def __str__(self):
        return self.user.username
    
    
class userAddress(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=30)
    
    def __str__(self):
        return self.user.username
    