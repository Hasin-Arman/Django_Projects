from django import forms
from django.core import validators
class contact_form(forms.Form):
    name=forms.CharField(label="username",initial="Arman",help_text="Total character must be at least 10 character",widget=forms.Textarea(attrs={'id': 'username','placeholder': 'please enter your username'}))
    email=forms.CharField(label="user email",widget=forms.EmailInput())
    files=forms.FileField()
    age=forms.IntegerField()
    date=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.CharField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    weight=forms.FloatField()
    check=forms.BooleanField()
    CHOICE=[('S','small'),('M','medium'),('L','large')]
    size=forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect())
    CHOOSE=[('M','male'),('F','female'),('O','other')]
    gender=forms.MultipleChoiceField(choices=CHOOSE,widget=forms.CheckboxSelectMultiple())
 
def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("not enough")   
    
class student_form(forms.Form):
    name=forms.CharField(widget=forms.TextInput(),validators=[validators.MinLengthValidator(10,message="Enter at least 10 characters")])
    text=forms.CharField(widget=forms.TextInput(),validators=[len_check])
    email=forms.CharField(widget=forms.EmailInput(),validators=[validators.EmailValidator(message="Enter a valid email address")])
    age=forms.IntegerField(validators=[validators.MinValueValidator(25,message="value must be min 25"),validators.MaxValueValidator(35,message="value must be max 35")])
    files=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpg'],message="please enter a valid file")])
    
    # def clean_name(self):
    #     valname=self.cleaned_data["name"]
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a username")
    #     return valname
    
    # def clean_email(self):
    #     valEmail=self.cleaned_data["email"]
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Please enter valid email address")
    #     return valEmail
    # def clean(self):
        # cleaned_data =super().clean()
        # valname = self.cleaned_data["name"]
        # valemail = self.cleaned_data["email"]
        # if len(valname) < 10:
        #     raise forms.ValidationError("Enter a valid username")
        # if '.com' not in valemail:
        #     raise forms.ValidationError("Please enter valid email address")
   
    # name=forms.CharField()
    # password=forms.CharField(widget=forms.PasswordInput)
    # con_password=forms.CharField(widget=forms.PasswordInput)
    # def clean(self):
        # cleaned_data = super().clean()
        # passVal=self.cleaned_data["password"]
        # con_pass=self.cleaned_data["con_password"]
        
        # if passVal != con_pass:
        #     raise forms.ValidationError("password does not match")
        
            
    