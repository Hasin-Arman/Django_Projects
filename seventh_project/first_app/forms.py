from django import forms
from first_app.models import students

class StudentForm(forms.ModelForm):
    class Meta:
        model=students
        fields="__all__"
        
        labels={
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'})
        }
        
        error_messages={
            'name':{'required':'Name must be provided'}
        }
        
        