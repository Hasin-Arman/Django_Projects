from django.urls import path
from first_app.views import home,showData

urlpatterns = [
    path('',home,name='homepage'),
    path('show/',showData)
]