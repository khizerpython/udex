from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.urls import reverse
from django.template.loader import render_to_string
from django.core import mail
from web_app.models import Menus, AirwayBill
from web_app.forms import GetManifestForm, AirwayBillManifestCheckedForm
from web_app.constants import *
from web_app.core.view_base import BaseViewForAuthenticatedClass, BaseViewForAuthenticatedClassForJsonResponse

import os
import json
from inspect import currentframe, getframeinfo
from datetime import datetime , time
import traceback
import sys

frameinfo = getframeinfo(currentframe())



class ListManifestView(ListView,BaseViewForAuthenticatedClass):
# class ListMenuView(ListView):
    template_name :str = 'manifest/list.html'
    model = Menus
    _page_title: str = "Manifest"

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        """ 
        
        context.update({'page_title':self._page_title})
        return super().render_to_response(context, **response_kwargs)
    
    
class GetManifestView(BaseViewForAuthenticatedClassForJsonResponse):

    def _making_airway_bill_as_list_obj(self, request, airwaybills):
        airway_bill_array = []

        for bill in airwaybills:
            bill_dict = {}

            # Extract regular fields
            for field in bill._meta.get_fields():
                if field.auto_created and not field.concrete:
                    continue

                field_name = field.name
                value = getattr(bill, field_name, None)

                if hasattr(value, "_meta"):
                    bill_dict[field_name] = str(value)
                else:
                    bill_dict[field_name] = value

            # Handle nested 'data' field if present
            data = getattr(bill, 'data', {})
            if isinstance(data, dict):
                # Extract hs_code and hs_title from invoice_details
                invoice_details = data.get('invoice_details', {})
                hs_codes = []
                hs_titles = []
                quantities = 0
                bill_total = 0

                for detail in invoice_details.values():
                    hs_code = detail.get('hs_code')
                    hs_title = detail.get('hs_title')
                    quantity = detail.get('quantity')
                    total = detail.get('total')
                    if hs_code:
                        hs_codes.append(hs_code)
                    if hs_title:
                        hs_titles.append(hs_title)
                    if quantity:
                        quantities = quantities + int(quantity)    
                    if total:
                        # bill_total = bill_total + int(total)  
                        bill_total = bill_total + float(total)
  

                bill_dict['hs_code'] = hs_codes
                bill_dict['hs_title'] = hs_titles
                bill_dict['quantites'] = quantities
                bill_dict['bill_total'] = bill_total

                # Extract volumetric_weight from dimensions
                dimensions = data.get('dimensions', {})
                volumetric_weights = []

                for dim in dimensions.values():
                    vw = dim.get('volumetric_weight')
                    if vw:
                        volumetric_weights.append(vw)

                bill_dict['volumetric_weight'] = volumetric_weights
                bill_dict['manifest_check_airwaybill'] = reverse('make_airway_bill_manifest')

            airway_bill_array.append(bill_dict)

        return airway_bill_array

    def _get(self, request, *args, **kwargs):
        form_validation =  GetManifestForm(data=request.POST)
        if form_validation.is_valid():
            from_date = form_validation.cleaned_data.get("from_date")
            to_date = form_validation.cleaned_data.get("to_date")

            datetime_start = datetime.combine(from_date, time.min)  # 00:00:00
            datetime_end = datetime.combine(to_date, time.max)      # 23:59:59.999999

            airway_bills = AirwayBill.objects.filter(
                created_at__gte=datetime_start,
                created_at__lt=datetime_end, 
                data__is_manifest=False
            ).select_related('service_id')

            bills = self._making_airway_bill_as_list_obj(request,airway_bills)
            return JsonResponse(data=bills, status=200, safe=False)

    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)      
    

class AirwayBillManifestCheckedView(BaseViewForAuthenticatedClassForJsonResponse):

    def post(self, request, *args, **kwargs):
        
        form_validation = AirwayBillManifestCheckedForm(request.POST)
        if form_validation.is_valid():
            cleaned_data = form_validation.cleaned_data 
            airway_bill_id = cleaned_data.get("id")
            bill_obj = AirwayBill.objects.filter(id=airway_bill_id).first()

            if bill_obj:
                # Update 'is_manifest' in the JSON field
                bill_data = bill_obj.data
                bill_data['is_manifest'] = True

                # Save the updated data back
                bill_obj.data = bill_data
                bill_obj.save()

                return JsonResponse({"detail": f"{bill_obj.tracking_number} has been updated successfully"}, status=200)