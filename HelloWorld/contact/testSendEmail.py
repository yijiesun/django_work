from django.core.mail import send_mail 
from django.http import HttpResponse
 
def sendEmail(request):
    send_mail('subject', 'this is the message of email', '489662100@qq.com',['sunyijie520@126.com'], fail_silently=False)
    return HttpResponse('successful')