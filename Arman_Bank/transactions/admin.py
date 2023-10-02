from django.contrib import admin
from .models import TransactionModel
# Register your models here.

class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approved']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance+=obj.amount
        obj.balance_after_transaction=obj.account.balance
        obj.account.save()
        super().save_model(request, obj, form, change)
    
admin.site.register(TransactionModel,TransactionModelAdmin)
