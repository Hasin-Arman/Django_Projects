from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_cart,name='cart'),
    path('<int:product_id>/',views.add_to_cart,name='add_cart'),
    path('remove/<int:product_id>/',views.remove_cart_item,name='remove'),
    path('removeCart/<int:product_id>/',views.remove_cart,name='removeCart'),
]