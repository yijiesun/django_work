from django.contrib import admin 
from django.conf.urls import url 
from django.urls import path 
from HelloWorld.view import hello 
urlpatterns = [ 
path('admin/', admin.site.urls), url('^hello/$', hello), ] 
