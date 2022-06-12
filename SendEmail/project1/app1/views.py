from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def SendMail(request):
    template_name='sendmail.html'
    context={}
    if request.method=='POST':
        subject = 'welcome'
        message = f'Hi, this is test mail.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email'), ]
        send_mail( subject, message, email_from, recipient_list )
    return render(request,template_name,context)