from django.urls import path
from . import views

urlpatterns = [
    path('Login/',views.HomeView.as_view() , name='Home'),
    path('users/',views.UserDetails.as_view() , name='UserDetails'),
]