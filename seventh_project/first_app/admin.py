from django.contrib import admin
from first_app.models import students,student_info,teacher_info,EmployeeModel,ManagerModel,Friend,Me,person,passport,post,Student,Teacher
# Register your models here.
# admin.site.register(students)
# admin.site.register(student_info)
# admin.site.register(teacher_info)
 
# @admin.register(EmployeeModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'city', 'designation']
    
# @admin.register(ManagerModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'city', 'designation','take_interview','hire']

# admin.site.register(person)
# admin.site.register(post)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name', 'roll', 'class_name']
    
@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display=['name', 'subject', 'phone','student_list']