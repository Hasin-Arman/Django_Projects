from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .constants import gender_type,Account_type
from .models import userBankAccountModel,userAddressModel
class userRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=gender_type)
    account_type = forms.ChoiceField(choices=Account_type)
    city = forms.CharField(max_length= 100)
    street_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date','gender', 'postal_code', 'city','country','street_address']
    def save(self,commit=True):
        our_user = super().save(commit=False)
        if commit==True:
            our_user.save()
            account_type=self.cleaned_data['account_type']
            birth_date=self.cleaned_data['birth_date']
            gender=self.cleaned_data['gender']
            city=self.cleaned_data['city']
            country=self.cleaned_data['country']
            postal_code=self.cleaned_data['postal_code']
            street_address=self.cleaned_data['street_address']
        
            userAddressModel.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address=street_address
            )
            userBankAccountModel.objects.create(
                user = our_user,
                account_type  = account_type,
                gender = gender,
                birth_date =birth_date,
                account_no = 10000 + our_user.id
            )
        return our_user
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
            })
            
class userUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=gender_type)
    account_type = forms.ChoiceField(choices=Account_type)
    city = forms.CharField(max_length= 100)
    street_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
            })
        if self.instance:
            try:
                user_account=self.instance.account
                user_address=self.instance.address
            except userBankAccountModel.DoesNotExist:
                user_account=None
                user_address=None
        
        if user_account:
            self.fields['account_type'].initial = user_account.account_type
            self.fields['gender'].initial = user_account.gender
            self.fields['birth_date'].initial = user_account.birth_date
            self.fields['street_address'].initial = user_address.street_address
            self.fields['city'].initial = user_address.city
            self.fields['postal_code'].initial = user_address.postal_code
            self.fields['country'].initial = user_address.country
        
    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            user_account,created=userBankAccountModel.objects.get_or_create(user=user)
            user_address,created=userAddressModel.objects.get_or_create(user=user)
            
            user_account.account_type=self.cleaned_data['account_type']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()
            
            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()
        return user            