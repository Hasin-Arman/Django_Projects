from django.contrib import admin
from .models import Product,productReview
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=['product_name', 'price', 'category','stock' ,'created_date', 'modified_date', 'is_available']
    prepopulated_fields={'slug':('product_name',)}
    
admin.site.register(Product,productAdmin)
admin.site.register(productReview)