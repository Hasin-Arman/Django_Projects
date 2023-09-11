
from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.contact ,name="contactpage" ),
    path('form/',views.submit_form ,name="formpage" ),
    path('django_form/',views.student,name="django_form" ),
    
]