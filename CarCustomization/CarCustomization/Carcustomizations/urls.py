# from django.contrib import admin
from django.urls import path, include   
from django.conf.urls import url
from .views import *

app_name='Carcustomizations'

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('search/',search,name='search'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    
]
