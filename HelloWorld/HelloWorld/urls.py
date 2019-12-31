from django.contrib import admin 
from django.conf.urls import url 
from django.urls import path 
from HelloWorld.view import current_datetime
from books import views
from contact.views import contact
from contact.testSendEmail import *
admin.autodiscover()

urlpatterns = [ 
url(r'^admin/',admin.site.urls,name='admin'),
url('^time/$', current_datetime),
url(r'^search-form/$', views.search_form),
url(r'^search/$', views.search),
url(r'^contact/$', contact),
url(r'^mail/$',sendEmail),
 ] 
