from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request,'home.html')
    # response.set_cookie('name','chayan',max_age=60)
    response.set_cookie('name','chayan',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookies(request):
    name=request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})

def del_cookies(request):
    response =render(request,'del_cookie.html')
    response.delete_cookie('name')
    return response

def set_sessions(request):
    data={
        'name':'Arman',
        'age':21,
        'language':'Bangla'
    }
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name')
        request.session.modified=True
        return  render(request,'get_session.html',{'data':name})
    else:
        return HttpResponse('your session has expired')

def del_session(request):
    request.session.flush()
    return render(request,'del_session.html')