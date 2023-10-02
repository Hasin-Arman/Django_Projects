from django.db import models

# Create your models here.
class stock_market_model(models.Model):
    date=models.CharField(max_length=30)
    trade_code=models.CharField(max_length=30)
    high=models.CharField(max_length=30)
    low=models.CharField(max_length=30)
    open=models.CharField(max_length=30)
    close=models.CharField(max_length=30)
    volume=models.CharField(max_length=30)