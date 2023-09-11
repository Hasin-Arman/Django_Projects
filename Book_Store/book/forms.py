from django import forms
from book.models import BookModel

class Book_Form(forms.ModelForm):
        class Meta:
                model = BookModel
                fields=['id','book_name','author','category']