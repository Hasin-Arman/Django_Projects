from django.http import HttpResponse

def home(request):
    return HttpResponse("""
                           <h1> This is Home page </h1>
                           <a href="/first_app/contact/">contact</a>
                           <a href="/first_app/about/">about</a>
                           <a href="/second_app/feedback/">feedback</a>
                           <a href="/second_app/courses/">courses</a>
                        """)