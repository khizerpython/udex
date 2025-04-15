from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, F, Value
from django.db.models.functions import Concat
from django.utils import timezone
from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from web_app.models.billings import AirwayBill
from web_app.forms.contact_us import ContactUsForm
# App level Import


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/homepage.html", {})


class DashboardPageView(View):

    def get(self, request, *args, **kwargs):
        # Get date 30 days ago from now
        thirty_days_ago = timezone.now() - timedelta(days=30)
        # Group by user and count airway bills

        result = (
            AirwayBill.objects
            .filter(created_at__gte=thirty_days_ago)
            .values(full_name=Concat(F('user_id__first_name'), Value(' '), F('user_id__last_name')))
            .annotate(count=Count('id'))
        )


        result_dict = {item['full_name']: item['count'] for item in result}
        print(result_dict)
        return render(request, "frontend/dashboard.html", {})

class AboutUsPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/about_us.html", {})

class ContactUsPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/contact_us.html", {})
    
    def post(self,request):
        data=request.POST
        form_validation = ContactUsForm(data)
        if form_validation.is_valid():
            cleaned_data = form_validation.cleaned_data
            subject = "UDEX Contact Us Email"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = settings.ADMIN_EMAIL_GET_CONTACT_US_EMAIL

            html_content = render_to_string("email_templates/contact_us_email.html", {
                'name': cleaned_data.get('name'),
                'contact': cleaned_data.get('contact'),
                'message': cleaned_data.get('reason'),
                
            })

            email = EmailMultiAlternatives(subject, "", from_email, [to_email])
            email.attach_alternative(html_content, "text/html")
            email.send()

            return render(request, "frontend/contact_us.html", {"success": True})
            
        else:
            pass
            return JsonResponse({"detail": f"Air way bill location can not initiated","errors": dict(form_validation.errors.items()), "errors_div": "initiate_"}, status=401)


class LocationView(View):
    def post(self,request):
            try:
                airway_bill_instance = AirwayBill.objects.get(tracking_number=request.POST.get('tracking_number'))
                location = airway_bill_instance.locations.all().order_by('-created_at')
                context = {
                    "obj":airway_bill_instance,
                    "locations":location
                }
                return render(request,template_name='frontend/locations.html',context=context)
            except ObjectDoesNotExist:
             context = {
                    "not_found":"Invalid Tracking Id",
                }
             return render(request,template_name='frontend/locations.html',context=context)