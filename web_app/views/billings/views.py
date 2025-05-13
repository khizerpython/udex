from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.generic import ListView
from web_app.core.view_base import BaseViewForAuthenticatedClass, BaseViewForAuthenticatedClassForJsonResponse

from web_app.models.billings import *
from web_app.forms.billings import BillingsForm , BillingsDetail, BillingsUpdateForm
import json
import datetime
from web_app.utils.global_methods import send_airway_bill_creation_email_to_transport_department
import uuid

# Example bill_id
bill_id = uuid.uuid4()  # or use an existing UUID if you have one



class AirwayBillView(BaseViewForAuthenticatedClass):

    def get(self, request):
        # <view logic>
        user = self.request.user
        services = Service.objects.all()
        payments = Payment.objects.all()
        shipments = ShipmentType.objects.all()
        if user.is_admin:

            airway_bills = AirwayBill.objects.all()
        else:
            airway_bills = AirwayBill.objects.filter(user_id=user)
        context = {
            'services': services,
            'payments':payments,
            'shipments':shipments,
            'airway_bills':airway_bills
        }
        return render(request,template_name='billings/list.html', context=context)
    
    

class CreateAirwayBillView(BaseViewForAuthenticatedClassForJsonResponse):

    def post(self,request):
        data=request.POST
        dimension = data.get('dimensions')
        invoice_details = data.get('invoice_details')
        form_validation = BillingsForm(data)
        if form_validation.is_valid():
            form_validation.cleaned_data['data'] = {'dimensions': dimension, 'invoice_details': invoice_details}
            form_validation.cleaned_data['user_id'] = self.request.user
            tracking_number = form_validation.cleaned_data.get('tracking_number')
            obj = AirwayBill.objects.create(**form_validation.cleaned_data)

            sent_email = send_airway_bill_creation_email_to_transport_department(airway_way_data = form_validation.cleaned_data, request=request)
            if sent_email ==1:
                
                return JsonResponse({"detail": f"Air way bill with tracking ID {tracking_number} has been initiated successfully"}, status=200)
            else:
                 return JsonResponse({"detail": f"Air way bill with tracking ID {tracking_number} has been initiated successfully, but email didnt sent. Kindly contact transport department and tell them manually."}, status=200)
        else:
            return JsonResponse({"detail": f"Air way bill  can not initiated","errors": dict(form_validation.errors.items()), "errors_div": "create_"}, status=401)

class UpdateAirwayBillView(BaseViewForAuthenticatedClassForJsonResponse):
    
    def post(self,request):
        data=request.POST
        dimension = data.get('dimensions')
        id = data.get('id')
        invoice_details = data.get('invoice_details')
        
        form_validation = BillingsUpdateForm(data)
        if form_validation.is_valid():
            obj = AirwayBill.objects.get(id=id)
            tracking_number = obj.tracking_number
            if obj:
                obj.user_id = self.request.user
                obj.data = {'dimensions': dimension, 'invoice_details': invoice_details}
                obj.service_id = form_validation.cleaned_data.get('service_id')
                obj.shipper_company_name = form_validation.cleaned_data.get('shipper_company_name')
                obj.shipper_contact_person = form_validation.cleaned_data.get('shipper_contact_person')
                obj.shipper_reference = form_validation.cleaned_data.get('shipper_reference')
                obj.shipper_address = form_validation.cleaned_data.get('shipper_address')
                obj.shipper_state = form_validation.cleaned_data.get('shipper_state')
                obj.shipper_city = form_validation.cleaned_data.get('shipper_city')
                obj.shipper_post_code = form_validation.cleaned_data.get('shipper_post_code')
                obj.shipper_mobile_number = form_validation.cleaned_data.get('shipper_mobile_number')
                obj.shipper_phone_number = form_validation.cleaned_data.get('shipper_phone_number')
                obj.shipper_ntn_cnic = form_validation.cleaned_data.get('shipper_ntn_cnic')
                # obj.shipper_email_address = form_validation.cleaned_data.get('shipper_email_address')
                # reciever
                obj.reciever_company_name = form_validation.cleaned_data.get('reciever_company_name')
                obj.reciever_contact_person = form_validation.cleaned_data.get('reciever_contact_person')
                obj.reciever_address = form_validation.cleaned_data.get('reciever_address')
                obj.reciever_country = form_validation.cleaned_data.get('reciever_country')
                obj.reciever_state = form_validation.cleaned_data.get('reciever_state')
                obj.reciever_city = form_validation.cleaned_data.get('reciever_city')
                obj.reciever_post_code = form_validation.cleaned_data.get('reciever_post_code')
                obj.reciever_mobile_number = form_validation.cleaned_data.get('reciever_mobile_number')
                obj.reciever_phone_number = form_validation.cleaned_data.get('reciever_phone_number')
                obj.reciever_email = form_validation.cleaned_data.get('reciever_email')
                obj.eori_number = form_validation.cleaned_data.get('eori_number')
                # obj.reciever_fax = form_validation.cleaned_data.get('reciever_fax')
                obj.payment_id = form_validation.cleaned_data.get('payment_id')
                obj.shipment_id = form_validation.cleaned_data.get('shipment_id')
                # obj.fedex_number = form_validation.cleaned_data.get('fedex_number')
                obj.weight = form_validation.cleaned_data.get('weight')
                obj.pieces = form_validation.cleaned_data.get('pieces')
                obj.save()
                

                
                return JsonResponse({"detail": f"Air way bill with tracking ID {tracking_number} has been updated successfully"}, status=200)
                
            else:
                return JsonResponse({"detail": f"Air way bill with tracking ID {tracking_number} not found"}, status=401)
        else:
            return JsonResponse({"detail": f"Air way bill with tracking ID {id} can not initiated","errors": dict(form_validation.errors.items()), "errors_div": "update_"}, status=401)


class GetSpecificBillingDetails(BaseViewForAuthenticatedClassForJsonResponse):

    def custom_serializer(self, obj):
        serialized_obj = serializers.serialize("python", [obj])[0]
        fields = serialized_obj['fields']
        # Convert datetime fields to string representation
        for field_name, field_value in fields.items():
            if isinstance(field_value, datetime.datetime):
                fields[field_name] = field_value.strftime('%Y-%m-%d %H:%M:%S')  # Adjust the format as needed


        fields['shipment_id'] = obj.shipment_id.name  
        fields['payment_id'] = obj.payment_id.name
        fields['service_id'] = obj.service_id.name
        return fields

    def _get(self, request, *args, **kwargs):
        data=request.POST
        form_validation = BillingsDetail(data=data)
        if form_validation.is_valid():
            id: str = form_validation.cleaned_data.get("id")
            detail_obj_queryset = AirwayBill.objects.get(id=id)
            detail_obj_json = json.dumps(self.custom_serializer(detail_obj_queryset))

            # detail_obj_json: list = json.loads(serializers.serialize("json", [detail_obj_queryset] ))
            # workflows_dict: dict = self._merge_objects(history_obj_json, history_obj_queryset)
            return JsonResponse(detail_obj_json, status=200, safe=False)
        
        return JsonResponse(data={"detail": "Invalid data found."}, status=401)

    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)


class GetDataToUpdateSpecificBill(BaseViewForAuthenticatedClassForJsonResponse):

    def _get(self, request, *args, **kwargs):
        data=request.POST
        form_validation = BillingsDetail(data=data)
        if form_validation.is_valid():
            id: str = form_validation.cleaned_data.get("id")
            detail_obj_queryset = AirwayBill.objects.get(id=id)
            # detail_obj_json = json.dumps(self.custom_serializer(detail_obj_queryset))

            detail_obj_json: list = json.loads(serializers.serialize("json", [detail_obj_queryset] ))
            # workflows_dict: dict = self._merge_objects(history_obj_json, history_obj_queryset)
            return JsonResponse({"data": detail_obj_json}, status=200, safe=False)
        
        return JsonResponse(data={"detail": "Invalid data found."}, status=401)

    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)
    
class ListOfAirwayBillsJsonFormat(BaseViewForAuthenticatedClassForJsonResponse):

    def _merge_objects(self, data: list, airway_bills) -> dict:
        
        return_data: dict = {}

        def iterate_object(obj_id: str):
            
            workflow_queryset_inst = airway_bills.get(id=obj_id)
            for key, value in return_data.get(obj_id, {}).items():
                if key == "service_id":
                    return_data[obj_id][key] = workflow_queryset_inst.service_id.name
                elif key == "payment_id":    
                    return_data[obj_id][key] = workflow_queryset_inst.payment_id.name
                elif key == "shipment_id":    
                    return_data[obj_id][key] = workflow_queryset_inst.shipment_id.name
                    
           
            return_data[obj_id]["detail_url"] = reverse("airway_bill_detail")
            return_data[obj_id]["update_url"] = reverse("get_specific_bill_to_update")
            return_data[obj_id]["label_url"] = reverse("create_airway_bill_label", kwargs={'bill_id': obj_id})

        for obj_from_list in data:
            obj_id: str = obj_from_list.get("pk", "")
            if obj_id not in return_data:
                return_data[obj_id] = obj_from_list.get("fields", {})
                return_data[obj_id]["service_id"] = "" # Initializing key to avoid RuntimeError `dictionary changed size during iteration`
                return_data[obj_id]["payment_id"] = "" # Initializing key to avoid RuntimeError `dictionary changed size during iteration`
                return_data[obj_id]["shipment_id"] = "" # Initializing key to avoid RuntimeError `dictionary changed size during iteration`
                iterate_object(obj_id)

        return return_data

    def get(self, request, *args, **kwargs):
        user = self.request.user
        airway_bills = AirwayBill.objects.filter(user_id=user)
        serialize_workflows: list = json.loads(serializers.serialize("json", queryset=airway_bills))
        workflows_dict: dict = self._merge_objects(serialize_workflows, airway_bills)
        return JsonResponse(data=workflows_dict, status=200)    
    
# Create and download airway bill label
class CreateAirwayBillLabelView(BaseViewForAuthenticatedClassForJsonResponse):

    def get(self, request, bill_id):
        bill = AirwayBill.objects.get(id=bill_id)
        # total_price = sum(int(detail.get('price')) for detail in bill.data.get('invoice_details').values())
        total_price = sum(float(detail.get('total')) for detail in bill.data.get('invoice_details').values())
        volumetric_Weight = sum(float(detail.get('volumetric_weight')) for detail in bill.data.get('dimensions').values())

        # dimensions = bill.data.get('dimensions')
        # volumetric_dimension = 0 
        # for key,value in dimensions.items():
        #     multiplicated_obj = float(value.get('length')) * float(value.get('width')) * float(value.get('height'))
        #     dimension =  multiplicated_obj / 5000
        #     volumetric_dimension = volumetric_dimension + dimension

        context_dict = {
            'bill':bill,
            'total_price':total_price,
            'volumetric_dimension':volumetric_Weight
        }     
        return render(request,template_name='billings/download_label.html',context=context_dict) 