from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.userRegistrationView.as_view(),name='register'),
    path('login/',views.userLoginView.as_view(),name='login'),
    path('logout/',views.userLogoutView.as_view(),name='logout'),
    path('update/',views.userUpdateView.as_view(),name='update'),
]
