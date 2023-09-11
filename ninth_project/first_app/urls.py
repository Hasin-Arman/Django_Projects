from django.urls import path
from first_app.views import home,get_cookies,del_cookies,set_sessions,get_session,del_session
urlpatterns = [
    # path('',home),
    path('',set_sessions),
    path('get/',get_session),
    path('del/',del_session)
]