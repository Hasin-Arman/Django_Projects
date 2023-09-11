from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_form,student_form
# Create your views here.
def contact(request):
    context = {
        "name":"phitron",
        "age":19,
        "marks":70,
        "courses":[
            {
                "id":1,
                "course":"C++",
                "teacher":"Arman"
            },
            {
                "id" : 2,
                "course" : "C",
                "teacher" : "Rahim"
            },
            {
                "id" : 3,
                "course" : "Python",
                "teacher" : "Fahim"
            }
        ],
        "lst" : [24,3,10,5], 
        "blog" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Harum quae tempora fugit laborum voluptas mollitia. Explicabo earum assumenda obcaecati et.",
        }
    if request.method =='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        return render(request, './first_app/new.html',{'name':name, 'pwd':pwd})
    else:
        return render(request, './first_app/new.html')

def submit_form(request):
    return render(request, './first_app/form.html')

def django_form(request):
    if request.method == 'POST':
        form=contact_form(request.POST,request.FILES)
        if form.is_valid():
            file=form.cleaned_data['files']
            with open("./first_app/upload/ " + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contact_form()
    return render(request, 'first_app/django_form.html',{'form':form})
    
def student(request):
    if request.method == 'POST':
        form=student_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = student_form()
    return render(request, 'first_app/django_form.html',{'form':form})