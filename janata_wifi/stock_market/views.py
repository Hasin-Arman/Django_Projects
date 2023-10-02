from django.shortcuts import render
from .models import stock_market_model
# Create your views here.
def home(request):
    data=stock_market_model.objects.all()
    return render(request,'index.html')