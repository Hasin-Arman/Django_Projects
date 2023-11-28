from django.shortcuts import render
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
from django.views.generic import CreateView
from .forms import ReviewForm
from .models import productReview
# Create your views here.
def product_detail(request,product_slug,category_slug):
    single_product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    review=productReview.objects.all()
    if request.user.is_authenticated:
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product=single_product
            form.save()
            form=ReviewForm()
        else:
            form=ReviewForm()
        return render(request,'product-detail.html',{'product':single_product,'form':form,'review':review})
    return render(request,'product-detail.html',{'product':single_product,'review':review})

def product_store(request,category_slug=None):
    if category_slug:
        category=Category.objects.get(slug=category_slug)
        products=Product.objects.filter(category=category,is_available=True)
        page=request.GET.get('page')
        paginator=Paginator(products,2)
        paged_products=paginator.get_page(page)
    else:
        searchItems=request.POST.get('search_item')
        if searchItems:
            products=Product.objects.filter(is_available=True,slug__icontains=searchItems)
            page=request.GET.get('page')
            paginator=Paginator(products,2)
            paged_products=paginator.get_page(page)
        else:
            products=Product.objects.filter(is_available=True)
            page=request.GET.get('page')
            paginator=Paginator(products,3)
            paged_products=paginator.get_page(page)
    category=Category.objects.all()
    return render(request,'store.html',{'products':paged_products,'category':category})



    