from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    father_name=models.CharField(max_length=20)
    address=models.TextField()
    
    def __str__(self):
        return self.name
    
# abstract base class inheritence
class common_info(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    class Meta:
        abstract = True

class student_info(common_info):
    roll=models.IntegerField()
    payment=models.IntegerField()
    section=models.CharField(max_length=10)

class teacher_info(common_info):
    salary=models.IntegerField()
    

# multitable inheritance
class EmployeeModel(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    class Meta:
        ordering = ['id']
        
class ManagerModel(EmployeeModel):
    take_interview=models.BooleanField()
    hire=models.BooleanField()
    
#proxy model
class Friend(models.Model):
    school = models.CharField(max_length=30)
    section=models.CharField(max_length=20)
    attendence=models.BooleanField()
    hw=models.CharField(max_length=50)

class Me(Friend):
    class Meta:
        proxy=True
    
#one to one relationship
class person(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
class passport(models.Model):
    user=models.OneToOneField(to=person, on_delete=models.CASCADE)
    page=models.IntegerField()
    validity=models.IntegerField()
    
#one to many relationship
class post(models.Model):
    user=models.ForeignKey(person, on_delete=models.SET_NULL,null=True)
    caption=models.CharField(max_length=30)
    details=models.CharField(max_length=40)

#many to many relationship
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    class_name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    student=models.ManyToManyField(Student,related_name='teachers')
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    
    def student_list(self):
        return ','.join(str(i) for i in self.student.all())
    def __str__(self):
        return self.name