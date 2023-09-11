from django.contrib import admin
from book.models import BookModel
# Register your models here.

class BookStoreModel(admin.ModelAdmin):
    list_display =('id','book_name','author','category','first_pub','last_pub')
admin.site.register(BookModel,BookStoreModel)