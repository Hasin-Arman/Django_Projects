from django import forms
from .models import productReview
class ReviewForm(forms.ModelForm):
    class Meta:
        model=productReview
        exclude=['user','product']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control w-75'
            })
    