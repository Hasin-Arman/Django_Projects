from django.urls import path
from . import views

urlpatterns = [
    path('<slug:product_slug>/<slug:category_slug>/',views.product_detail,name='details'),
    path('',views.product_store,name='store'),
    path('<slug:category_slug>/',views.product_store,name='category'),
]