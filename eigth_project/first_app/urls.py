from django.urls import path
from first_app.views import Signup,home,profile,Login,Logout,pass_change,pass_change2

urlpatterns = [
    path('',home,name='homepage'),
    path('signup/',Signup,name='sign'),
    path('login/',Login,name='login_page'),
    path('logout/',Logout,name='logout_page'),
    path('profile/',profile,name='profile_page'),
    path('change_pass/',pass_change,name='update_pass'),
    path('change_pass2/',pass_change2,name='update_pass2'),
]