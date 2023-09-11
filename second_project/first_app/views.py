from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse("""
                           <h1> This is about page </h1>
                           <a href="/first_app/contact/">contact</a>
                           <a href="/second_app/courses/">courses</a>
                           <a href="/second_app/feedback/">feedback</a>
                        
                        """)

def contact(request):
    return HttpResponse("""
                           <h1> This is contact page </h1>
                           <a href="/first_app/about/">about</a>
                           <a href="/second_app/courses/">courses</a>
                           <a href="/second_app/feedback/">feedback</a>
                        """)
