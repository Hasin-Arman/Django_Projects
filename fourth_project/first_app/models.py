from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    age = models.IntegerField()
    grade=models.FloatField()
    address=models.CharField(max_length=30,default="Dhaka")

    def __str__(self):
        return f"{self.name}-{self.roll}"
    
