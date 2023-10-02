from django.contrib import admin
from .models import userAddress,userBankAccount
# Register your models here.
admin.site.register(userAddress)
admin.site.register(userBankAccount)