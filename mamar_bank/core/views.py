from django.shortcuts import render
# from django.views.generic import TemplateView
# Create your views here.
def HomeView(request):
    return render(request,'index.html')