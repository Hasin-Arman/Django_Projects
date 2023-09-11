from django.contrib import admin
from .models import userAddressModel,userBankAccountModel
# Register your models here.
admin.site.register(userAddressModel)
admin.site.register(userBankAccountModel)
