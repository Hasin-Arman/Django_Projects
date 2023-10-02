from django import forms
from .models import TransactionModel
class TransactionForm(forms.ModelForm):
    class Meta:
        model=TransactionModel
        fields=['amount','transaction_type']
    
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__( *args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()
        
    def save(self,commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()

class depositForm(TransactionForm):
    def clean_amount(self):
        min_deposit = 500
        amount=self.cleaned_data["amount"]
        if(amount < min_deposit):
            forms.ValidationError(f'You need to deposit at least {min_deposit} $')
        return amount

class withdrawForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        max_withdraw = 15000
        min_withdraw =500
        balance = self.account.balance
        amount = self.cleaned_data["amount"]
        if(amount > balance):
            raise forms.ValidationError(f'you have {balance}$ in you account')
        elif(amount < min_withdraw):
            raise forms.ValidationError(f'you can withdraw min {min_withdraw}')
        elif(amount > max_withdraw):
            raise forms.ValidationError(f'you can withdraw max {max_withdraw}')
        return amount
    
class loanForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        return amount
        
        
        
    