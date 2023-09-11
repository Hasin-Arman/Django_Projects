from django.shortcuts import render
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
# Create your views here.
def product_detail(request,product_slug,category_slug):
    single_product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    return render(request,'product-detail.html',{'product':single_product})

def product_store(request,category_slug=None):
    if category_slug:
        category=Category.objects.get(slug=category_slug)
        products=Product.objects.filter(category=category)
        page=request.GET.get('page')
        paginator=Paginator(products, 1)
        paged_products=paginator.get_page(page)
    else:    
        products=Product.objects.filter(is_available=True)
        page=request.GET.get('page')
        paginator=Paginator(products, 2)
        paged_products=paginator.get_page(page)
    category=Category.objects.all()
    return render(request,'store.html',{'products':paged_products,'category':category})

