from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from transaction.models import E_cash

def Send_Email(request):
    
    send_mail(
        subject='Transaction',
        message='Transaction Complete',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS])
