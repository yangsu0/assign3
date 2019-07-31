from django.urls import path
import blog.views
from django.contrib import admin

app_name='blog'

urlpatterns = [
    
    path('',blog.views.home, name='home'),
    path('new/',blog.views.new, name='new'),
    path('create/',blog.views.create, name='create'),
    path('portfolio/',blog.views.portfolio, name='portfolio'),
    path('newblog/',blog.views.blogpost, name='newblog'),
]