from django.urls import path
from . import views

urlpatterns = [
    path('orderComplete/',views.order_complete,name='complete'),
    path('placeOrder/',views.checkout,name='place'),
    path('success/',views.success_view,name='success'),
]