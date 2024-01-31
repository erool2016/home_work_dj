
from django.contrib import admin
from django.urls import path
from my_app.views import index, about

app_name = 'my_app'

urlpatterns = [

    path('',index,name='index'),
    path('about/',about,name='about'),
]