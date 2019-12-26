from django.contrib import admin 
from django.conf.urls import url 
from django.urls import path 
from HelloWorld.view import current_datetime

urlpatterns = [ 
path('admin/', admin.site.urls),
url('^time/$', current_datetime),] 
