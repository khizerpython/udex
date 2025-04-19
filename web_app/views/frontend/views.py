from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, F, Value
from django.db.models.functions import Concat
from django.utils import timezone
from datetime import timedelta, datetime

from django.db.models.functions import TruncMonth
from collections import OrderedDict
from dateutil.relativedelta import relativedelta

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from calendar import month_abbr


import calendar
from collections import defaultdict


from web_app.models.billings import AirwayBill
from web_app.forms.contact_us import ContactUsForm
# App level Import


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        
        return render(request, "frontend/homepage.html", {})


class DashboardPageView(View):

    def get_records_for_admin_user(self,request,*args,**kwargs):
        # Get current date and 8 months ago
        now = timezone.now()
        start_date = now - relativedelta(months=7)
        start_date = start_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        # List of last 5 months (datetime objects)
        # Create list of last 5 months with month abbreviations and datetime ranges
        months = []
        now = timezone.now()

        for i in range(4, -1, -1):
            month_date = now - relativedelta(months=i)
            months.append(month_date.replace(day=1))

        # ============================================= pie chart query ==============================================
        # Get date 30 days ago from now
        thirty_days_ago = timezone.now() - timedelta(days=30)
        # Group by user and count airway bills
        result = (
            AirwayBill.objects
            .filter(created_at__gte=thirty_days_ago)
            .values(full_name=Concat(F('user_id__first_name'), Value(' '), F('user_id__last_name')))
            .annotate(count=Count('id'))
        )
        pie_chart_labels = []
        pie_chart_series = []
        if result:
            pie_chart_labels = [item['full_name'] for item in result]
            pie_chart_series = [item['count'] for item in result]
        else:
            # Fallback for no data
            pie_chart_labels = ["No data"]
            pie_chart_series = [1]
        # ============================================================= line chart query ==============================================
        # Get all airway bills from the last 8 months
        bills = AirwayBill.objects.filter(created_at__gte=start_date)
        # Prepare month names and counts
        month_counts = OrderedDict()

        # Loop through each of the last 8 months
        for i in range(8):
            month_start = (start_date + relativedelta(months=i))
            month_end = (month_start + relativedelta(months=1))

            month_name = month_abbr[month_start.month]  # Jan, Feb, Mar...

            count = bills.filter(created_at__gte=month_start, created_at__lt=month_end).count()
            month_counts[month_name] = count

        # Split into two separate lists
        line_chart_month_labels = list(month_counts.keys())
        line_chart_month_series = list(month_counts.values())

        # ==================================== Columns chart query ================
        # Prepare month labels
        column_month_labels = [calendar.month_abbr[m.month] for m in months]

        # Prepare month range pairs: [(start1, end1), (start2, end2), ...]
        month_ranges = []
        for i in range(5):
            start = months[i]
            if i < 4:
                end = months[i + 1]
            else:
                end = (start + timedelta(days=32)).replace(day=1)
            month_ranges.append((start, end))

        # Fetch all airway bills in last 5 months
        earliest_date = months[0]
        airway_bills = AirwayBill.objects.filter(created_at__gte=earliest_date).annotate(
            full_name=Concat(F('user_id__first_name'), Value(' '), F('user_id__last_name'))
        )

        # Organize counts per user per month
        user_month_count = defaultdict(lambda: [0] * 5)

        for ab in airway_bills:
            full_name = ab.full_name
            created = ab.created_at

            # Find month index
            for idx, (start, end) in enumerate(month_ranges):
                if start <= created < end:
                    user_month_count[full_name][idx] += 1
                    break

        # Prepare series for chart
        column_chart_series = [
            {'name': user, 'data': counts} for user, counts in user_month_count.items()
        ]



        context={
            'line_chart_month_labels':line_chart_month_labels,
            'line_chart_month_series':line_chart_month_series,
            'pie_chart_labels':pie_chart_labels,
            'pie_chart_series':pie_chart_series,
            'column_month_labels':column_month_labels,
            'column_chart_series':column_chart_series

        }
        return context


    def get_airwaybill_counts(self,request):
        # Get the current logged-in user
        user=request.user
        now = timezone.now()
        months = []
        counts = []

        for i in range(4, -1, -1):  # Last 5 months, oldest to latest
            month_start = (now.replace(day=1) - relativedelta(months=i))
            next_month = month_start + relativedelta(months=1)

            count = AirwayBill.objects.filter(
                user_id=user,
                created_at__gte=month_start,
                created_at__lt=next_month
            ).count()

            months.append(month_start.strftime('%b'))
            counts.append(count)
        
        # Now, 'months' will have the month names and 'counts' will have the corresponding counts
        context={
            'donut_chart_labels':months,
            'donut_chart_series':counts

        }
        return context

    def get(self, request, *args, **kwargs):
        
        if request.user.is_user_admin:
            context = self.get_records_for_admin_user(request)
        else:
            context = self.get_airwaybill_counts(request)

        
        return render(request, "frontend/dashboard.html", context=context)

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