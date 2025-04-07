from django.views import View
from django.shortcuts import render


from django.core.exceptions import ObjectDoesNotExist
from web_app.models.billings import AirwayBill

# App level Import


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/homepage.html", {})


class DashboardPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/dashboard.html", {})


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