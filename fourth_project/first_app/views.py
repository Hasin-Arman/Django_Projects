from django.shortcuts import render,redirect
from first_app.models import studentModel
# Create your views here.
def home(request):
    students = studentModel.objects.all()
    return render(request,'index.html',{'data':students})

def delete_student(request,roll):
    std=studentModel.objects.get(pk=roll).delete()
    return redirect('homepage')
    
    
