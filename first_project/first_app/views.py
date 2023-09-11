from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is the home page</h1>")

def about(request):
    return HttpResponse("This is the about page")






