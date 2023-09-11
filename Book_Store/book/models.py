from django.db import models

# Create your models here.
class BookModel(models.Model):
    category=(
        ('Mystry','Mystry'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
    )
    id = models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=20,choices=category)
    first_pub=models.DateTimeField(auto_now_add=True)
    last_pub=models.DateTimeField(auto_now=True)
    
