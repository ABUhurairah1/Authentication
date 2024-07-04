from django.urls import path
from .views import *

urlpatterns = [
    path("",Home,name='Home'),
    path('login-page/',Login,name='Login'),
    path('sign-in/',Sign_in,name='Sign-in'),
    path('logout/',Logout,name='Logout'),
]