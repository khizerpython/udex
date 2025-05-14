from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse
from django.core import serializers
from django.urls import reverse

from web_app.models.billings import AirwayBillLocation,AirwayBill
from web_app.forms.billings import BillingsForm , BillingsDetail, BillingsUpdateForm, BillingLocationForm,GetBillingsLocationDetailsForm
import json
from web_app.constants import RIDER_DEPARTMENT_ID


class ListAirwayBillLocationView(View):

    def get(self, request):
        # <view logic>
        user = self.request.user
        if user.department_id.all().first().id == RIDER_DEPARTMENT_ID:
            airway_bills = AirwayBill.objects.all().order_by("-updated_at")
        else:
            airway_bills = AirwayBill.objects.filter(user_id=user)
        context = {
            'airway_bills':airway_bills
        }
        return render(request,template_name='billing_locations/list.html', context=context)
    
    
class AirwayBillLocationView(View):
    
    def post(self,request):
        data=request.POST
        form_validation = BillingLocationForm(data)
        if form_validation.is_valid():
            location = form_validation.cleaned_data.get('name')
            bill = form_validation.cleaned_data.get('airway_bill_id')
            AirwayBillLocation.objects.create(**form_validation.cleaned_data)
            return JsonResponse({"detail": f"Air way bill location {location} for tracking ID {bill.tracking_number} has been initiated successfully"}, status=200)
        else:
            pass
            return JsonResponse({"detail": f"Air way bill location can not initiated","errors": dict(form_validation.errors.items()), "errors_div": "initiate_"}, status=401)



class AirwayBillLocationDetailsView(View):
        
        def _merge_objects(self, data: list, airway_bills) -> dict:
        
            return_data: dict = {}

            def iterate_object(obj_id: str):
                return_data[obj_id]["data_url"] = reverse("delete_airway_bill_locations")

            for obj_from_list in data:
                obj_id: str = obj_from_list.get("pk", "")
                if obj_id not in return_data:
                    return_data[obj_id] = obj_from_list.get("fields", {})
                    return_data[obj_id]["data_url"] = "" # Initializing key to avoid RuntimeError `dictionary changed size during iteration`
                    iterate_object(obj_id)

            return return_data
    
        def _get(self, request, *args, **kwargs):
            data=request.POST
            form_validation = GetBillingsLocationDetailsForm(data=data)
            if form_validation.is_valid():
                airway_bill_id = form_validation.cleaned_data.get('airway_bill_id')
                detail_obj_queryset = AirwayBillLocation.objects.filter(airway_bill_id=airway_bill_id)
                detail_obj_json: list = json.loads(serializers.serialize("json", detail_obj_queryset ))
                workflows_dict: dict = self._merge_objects(detail_obj_json, detail_obj_queryset)
                return JsonResponse(workflows_dict, status=200, safe=False)
            
            return JsonResponse(data={"detail": "Invalid data found."}, status=401)

        def post(self, request, *args, **kwargs):
            return self._get(request, *args, **kwargs)

class AirwayBillLocationDeleteView(View):
        def _get(self, request, *args, **kwargs):
            data=request.POST
            form_validation = GetBillingsLocationDetailsForm(data=data)
            if form_validation.is_valid():
                try:
                    airway_bill_id = form_validation.cleaned_data.get('airway_bill_id')
                    location_obj = AirwayBillLocation.objects.get(id=airway_bill_id).delete()

                    return JsonResponse(data={"detail": "Location Has been deleted."}, status=200, safe=False)
                except:
                    return JsonResponse(data={"detail": "Location can not be deleted."}, status=200, safe=False)
            
            return JsonResponse(data={"detail": "Invalid data found."}, status=401)

        def post(self, request, *args, **kwargs):
            return self._get(request, *args, **kwargs)



class DownloadAirwayBillView(View):

    def get(self, request, bill_id):
        bill = AirwayBill.objects.get(id=bill_id)
        volumetric_Weight = sum(float(detail.get('volumetric_weight')) for detail in bill.data.get('dimensions').values())
        total_price = sum(float(detail.get('total')) for detail in bill.data.get('invoice_details').values())

        context_dict = {
            'bill':bill,
            'total_price':total_price,
            'volumetric_Weight':volumetric_Weight
        }        
        return render(request,template_name='billing_locations/download_billings.html',context=context_dict)
