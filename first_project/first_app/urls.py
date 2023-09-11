from django.urls import path,include
from . import views
from django.contrib import admin
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
]