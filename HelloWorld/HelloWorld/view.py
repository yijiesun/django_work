from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return render(request, 'current_datetime.html',{'page_path':str(request.path),'agent_path':str(ua),'ip_address':str(request.META['REMOTE_ADDR']),'current_date':str(now)})