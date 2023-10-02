from django.db import models
from accounts.models import userBankAccount
# Create your models here.
Deposit=1
Withdraw=2
Loan=3
Loan_paid=4

TRANSACTION_TYPE =(
    (Deposit,"deposit"),
    (Withdraw,"withdraw"),
    (Loan,"loan"),
    (Loan_paid,"loan_paid")
)

class TransactionModel(models.Model):
    account=models.ForeignKey(userBankAccount,related_name='transactions',on_delete=models.CASCADE)
    amount=models.IntegerField()
    balance_after_transaction=models.IntegerField()
    transaction_type=models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approved=models.BooleanField(default=False)
    
    class Meta:
        ordering = ['timestamp']