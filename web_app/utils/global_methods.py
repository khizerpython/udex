from django.template.loader import render_to_string

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