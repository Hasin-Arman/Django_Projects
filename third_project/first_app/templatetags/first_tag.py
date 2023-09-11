from django import template
from django.template.loader import get_template
register=template.Library()

def my_template(value,arg):
    if(arg=="change"):
        value ="chayan"
        return value
    if(arg=="title"):
        return value.title()


register.filter('change_name',my_template)

def show_course():
    course =[
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
        ]
    return {'courses': course}  
course_template = get_template('first_app/course.html')  
register.inclusion_tag(course_template)(show_course)
