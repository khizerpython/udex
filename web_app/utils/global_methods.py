from django.template.loader import render_to_string
from django.urls import resolve

from django.contrib.auth.models import AnonymousUser

from datetime import datetime

from django.core.mail import EmailMultiAlternatives

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_new_user_welcome_email(subject, to_email, data, request=None) -> int:
    html_message = render_to_string(template_name=f"email_templates/new_user_welcome.html", context=data, request=request)

    try:
        email_sent = EmailMultiAlternatives(subject=subject, body="UDEX Email Notification", to=[to_email])
        email_sent.attach_alternative(html_message, 'text/html')
        email_sent = email_sent.send()
    except Exception as e:
        email_sent = 0
    
    return email_sent


def send_generic_email(subject, to_email, data, request=None) -> int:
    if subject is None: 
        return 0
    
    html_message = render_to_string(template_name=f"email_templates/generic_notification.html", context=data, request=request)

    try:
        email_sent = EmailMultiAlternatives(subject=subject, body="UDEX Email Notification", to=[to_email] if isinstance(to_email, str) else to_email)
        email_sent.attach_alternative(html_message, 'text/html')
        email_sent = email_sent.send()
    except Exception as e:
        email_sent = 0
    
    
    return email_sent



def send_session_out_request_email(subject, to_email, request=None) -> int:
    if subject is None: 
        return 0
    
    path = request.path
    current_url = resolve(request.path_info).view_name
    if not isinstance(request.user,AnonymousUser):
        user = request.user.get_fullname
        error_details = f"{request.user.get_fullname} doesn't has the permission to access {current_url} i.e. {path}"
    else:    
        user="Anonymous User"
        error_details = "Invalid user session detected, The session token is either expired or invalid."
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data= {
        'user':user,
        'path':path,
        'filename':current_url,
        'errors':error_details,
        'date':dt_string,
        'user_ip' :get_client_ip(request)

    }


    html_message = render_to_string(template_name=f"session_out_error.html", context=data, request=request)

    try:
        email_sent = EmailMultiAlternatives(subject=subject, body="UDEX Email Notification", to=[to_email] if isinstance(to_email, str) else to_email)
        email_sent.attach_alternative(html_message, 'text/html')
        email_sent = email_sent.send()
    except Exception as e:
        email_sent = 0
    
    return email_sent
