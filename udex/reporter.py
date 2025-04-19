# Django Imports
from django.utils import log
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import resolve

# Other imports
from copy import copy
import sys
import os
import traceback
from datetime import datetime



class CustomAdminEmailHandler(log.AdminEmailHandler):
    
    def emit(self, record):
        try:
            request = record.request
            
            subject = "Error UDEX"
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
        subject = self.format_subject(subject)

        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        exc_type, _, exc_tb = sys.exc_info()
        exc_type.__name__ == 'NameError'
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        
        error_details = traceback.format_exc()
        user=request.user.id
        path = request.path
        current_url = resolve(request.path_info).view_name
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        context= {
            'user':user,
            'path':path,
            'filename':current_url,
            'errors':error_details,
            'date':dt_string,
            'type':exc_type.__name__

        }
        html_message = render_to_string("email_error.html",context,request=request)
        self.send_mail(subject, message="message body", fail_silently=True, html_message=html_message)

    