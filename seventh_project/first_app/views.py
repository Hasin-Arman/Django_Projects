from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import Student,Teacher

# Create your views here.
def home(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=StudentForm()
    return render(request,'index.html',{'forms':form})

def showData(request):
    teacher = Teacher.objects.get(name = 'zishad')
    students = teacher.student.all()
    for std in students:
        print(std.name)
    
    # student=Student.objects.get(name= 'chayan')
    # teachers=student.teachers.all()
    # for teacher in teachers:
    #     print(teacher.name)
    return render(request,'show_data.html')
    
