from django.contrib import admin 
from django.conf.urls import url 
from django.urls import path 
from HelloWorld.view import current_datetime
admin.autodiscover()

urlpatterns = [ 
url(r'^admin/',admin.site.urls,name='admin'),
url('^time/$', current_datetime),] 
