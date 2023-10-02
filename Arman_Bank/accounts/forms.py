from django import forms
from .models import userAddress, userBankAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
ACCOUNT_TYPE = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
)

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class userAccountForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=30)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
            'account_type', 'gender', 'birth_date', 'street_address', 'city', 'postal_code', 'country']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            account_type = self.cleaned_data['account_type']
            gender = self.cleaned_data['gender']
            birth_date = self.cleaned_data['birth_date']
            street_address = self.cleaned_data['street_address']
            city = self.cleaned_data['city']
            postal_code = self.cleaned_data['postal_code']
            country = self.cleaned_data['country']

            userBankAccount.objects.create(
                user=user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=1000000 + user.id
            )

            userAddress.objects.create(
                user=user,
                street_address=street_address,
                city=city,
                postal_code=postal_code,
                country=country
            )
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })


class UserUpdateForm(forms.ModelForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=30)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
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
                user_account = self.instance.account
                user_address = self.instance.address
            except:
                user_address = None
                user_address = None
                
            if user_account:
                self.fields['gender'].initial = user_account.gender
                self.fields['account_type'].initial = user_account.account_type
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['country'].initial = user_address.country
                self.fields['postal_code'].initial = user_address.postal_code
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account = userBankAccount.objects.get(user=user)
            user_address = userAddress.objects.get(user=user)
            
            user_account.gender = self.cleaned_data["gender"]
            user_account.account_type = self.cleaned_data["account_type"]
            user_account.birth_date = self.cleaned_data["birth_date"]
            user_account.save()
            
            user_address.street_address = self.cleaned_data["street_address"]
            user_address.city = self.cleaned_data["city"]
            user_address.country = self.cleaned_data["country"]
            user_address.postal_code = self.cleaned_data["postal_code"]
            user_address.save()
        return user
            
                                