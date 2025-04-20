from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ObjectDoesNotExist


from web_app.constants import USERNAME_REGEX
from web_app.models import regex
from django.contrib.auth import get_user_model
# from web_app.models import Service,ShipmentType,AirwayBill,Payment,AirwayBillLocation

class BillingsForm(forms.Form):
    service_id = forms.ChoiceField(choices=[])

    # Shipper table
    shipper_company_name = forms.CharField(max_length=255, required=True)
    shipper_contact_person = forms.CharField(max_length=255, required=True)
    shipper_reference = forms.CharField(max_length=255, required=True)
    shipper_address = forms.CharField(max_length=255, required=True)
    shipper_state = forms.CharField(max_length=255, required=True)
    shipper_city = forms.CharField(max_length=255, required=True)
    shipper_post_code = forms.CharField(required=False,max_length=255)
    shipper_mobile_number = forms.CharField(max_length=20,required=True)
    shipper_phone_number = forms.CharField(max_length=20,required=True)
    shipper_ntn_cnic = forms.CharField(max_length=255, required=True)
    # shipper_email_address = forms.EmailField(max_length=255, required=True)

    # Reciever table
    reciever_company_name = forms.CharField(max_length=255, required=True)
    reciever_contact_person = forms.CharField(max_length=255, required=True)
    reciever_address = forms.CharField(max_length=255, required=True)
    reciever_country = forms.CharField(max_length=255, required=True)
    reciever_state = forms.CharField(max_length=255, required=True)
    reciever_city = forms.CharField(max_length=255, required=True)
    reciever_post_code = forms.CharField(required=False,max_length=255)
    reciever_mobile_number = forms.CharField(max_length=20,required=True)
    reciever_phone_number = forms.CharField(max_length=20,required=True)
    reciever_email = forms.EmailField(max_length=255, required=True)
    eori_number = forms.CharField(max_length=255, required=False)
    # reciever_fax = forms.CharField(max_length=255, required=True)

    # Shipment Details
    # payment_id = forms.ChoiceField(choices=[])
    shipment_id = forms.ChoiceField(choices = [])

    # fedex_number = forms.CharField(max_length=255, required=True)
    weight = forms.CharField(required=True)
    pieces = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(BillingsForm, self).__init__(*args, **kwargs)
        
        # Populate the choices dynamically from the Service model
        self.services = Service.objects.all()
        self.payments = Payment.objects.all()
        self.shipments = ShipmentType.objects.all()
        self.fields['service_id'].choices = [(str(service.id), str(service)) for service in self.services]
        self.fields['payment_id'].choices = [(str(payment.id), str(payment)) for payment in self.payments]
        self.fields['shipment_id'].choices = [(str(shipment.id), str(shipment)) for shipment in self.shipments]

    def clean(self):
        
        cleaned_data: dict = super().clean()

        service_id = cleaned_data.get('service_id')
        payment_id = cleaned_data.get('payment_id')
        shipment_id = cleaned_data.get('shipment_id')
        if service_id:
            try:
                service_instance = self.services.get(id=service_id)
                cleaned_data['service_id'] = service_instance
            except Service.DoesNotExist:
                # Handle the case where the Service instance with the given UUID doesn't exist
                raise forms.ValidationError("Service with the specified UUID does not exist.")
            
        if payment_id:    
            try:
                # payment_instance = Payment.objects.get(id=payment_id)
                payment_instance = self.payments.get(id=payment_id)
                cleaned_data['payment_id'] = payment_instance
            except Payment.DoesNotExist:
                raise forms.ValidationError("Payment with the specified UUID does not exist.")
        
        if shipment_id:    
            try:
                # shipment_instance = ShipmentType.objects.get(id=shipment_id)
                shipment_instance = self.shipments.get(id=shipment_id)
                cleaned_data['shipment_id'] = shipment_instance
            except Payment.DoesNotExist:
                raise forms.ValidationError("Shipment type with the specified UUID does not exist.")



        # airway_bill = AirwayBill.objects.latest('created_at')
        try:
            airway_bill = AirwayBill.objects.latest('created_at')
        except ObjectDoesNotExist:
            airway_bill = None
        if airway_bill is not None:            
            cleaned_data['tracking_number'] = int(airway_bill.tracking_number + 1)
        else:    
            cleaned_data['tracking_number'] = int('82000000')
        return cleaned_data


class BillingsDetail(forms.Form):
    id = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(BillingsDetail, self).__init__(*args, **kwargs)
        
        # Populate the choices dynamically from the AirWayBill model
        self.bills = AirwayBill.objects.all()
        
        self.fields['id'].choices = [(str(bill.id), str(bill.id)) for bill in self.bills]


class BillingsUpdateForm(forms.Form):
    service_id = forms.ChoiceField(choices=[])

    # Shipper table
    shipper_company_name = forms.CharField(max_length=255, required=True)
    shipper_contact_person = forms.CharField(max_length=255, required=True)
    shipper_reference = forms.CharField(max_length=255, required=True)
    shipper_address = forms.CharField(max_length=255, required=True)
    shipper_state = forms.CharField(max_length=255, required=True)
    shipper_city = forms.CharField(max_length=255, required=True)
    shipper_post_code = forms.CharField(required=False,max_length=255)
    shipper_mobile_number = forms.CharField(max_length=20,required=True)
    shipper_phone_number = forms.CharField(max_length=20,required=True)
    shipper_ntn_cnic = forms.CharField(max_length=255, required=True)
    # shipper_email_address = forms.EmailField(max_length=255, required=True)

    # Reciever table
    reciever_company_name = forms.CharField(max_length=255, required=True)
    reciever_contact_person = forms.CharField(max_length=255, required=True)
    reciever_address = forms.CharField(max_length=255, required=True)
    reciever_country = forms.CharField(max_length=255, required=True)
    reciever_state = forms.CharField(max_length=255, required=True)
    reciever_city = forms.CharField(max_length=255, required=True)
    reciever_post_code = forms.CharField(required=False,max_length=255)
    reciever_mobile_number = forms.CharField(max_length=20,required=True)
    reciever_phone_number = forms.CharField(max_length=20,required=True)
    reciever_email = forms.EmailField(max_length=255, required=True)
    eori_number = forms.CharField(max_length=255, required=False)
    # reciever_fax = forms.CharField(max_length=255, required=True)

    # Shipment Details
    payment_id = forms.ChoiceField(choices=Payment.objects.all())
    shipment_id = forms.ChoiceField(choices = ShipmentType.objects.all())

    # fedex_number = forms.CharField(max_length=255, required=True)
    weight = forms.CharField(required=True)
    pieces = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(BillingsUpdateForm, self).__init__(*args, **kwargs)
        
        # Populate the choices dynamically from the Service model
        self.services = Service.objects.all()
        self.payments = Payment.objects.all()
        self.shipments = ShipmentType.objects.all()
        self.fields['service_id'].choices = [(str(service.id), str(service)) for service in self.services]
        self.fields['payment_id'].choices = [(str(payment.id), str(payment)) for payment in self.payments]
        self.fields['shipment_id'].choices = [(str(shipment.id), str(shipment)) for shipment in self.shipments]

    def clean(self):
        
        cleaned_data: dict = super().clean()

        service_id = cleaned_data.get('service_id')
        payment_id = cleaned_data.get('payment_id')
        shipment_id = cleaned_data.get('shipment_id')
        if service_id:
            try:
                # Fetch the Service instance using the UUID
                # service_instance = Service.objects.get(id=service_id)
                service_instance = self.services.get(id=service_id)
                cleaned_data['service_id'] = service_instance
            except Service.DoesNotExist:
                # Handle the case where the Service instance with the given UUID doesn't exist
                raise forms.ValidationError("Service with the specified UUID does not exist.")
            
        if payment_id:    
            try:
                # payment_instance = Payment.objects.get(id=payment_id)
                payment_instance = self.payments.get(id=payment_id)
                cleaned_data['payment_id'] = payment_instance
            except Payment.DoesNotExist:
                raise forms.ValidationError("Payment with the specified UUID does not exist.")
        
        if shipment_id:    
            try:
                # shipment_instance = ShipmentType.objects.get(id=shipment_id)
                shipment_instance = self.shipments.get(id=shipment_id)
                cleaned_data['shipment_id'] = shipment_instance
            except Payment.DoesNotExist:
                raise forms.ValidationError("Shipment type with the specified UUID does not exist.")

        return cleaned_data

class BillingLocationForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    position = forms.IntegerField(required=True)
    airway_bill_id = forms.ChoiceField(choices=[])


    def __init__(self, *args, **kwargs):
        super(BillingLocationForm, self).__init__(*args, **kwargs)
        
        # Populate the choices dynamically from the Service model
        self.airway_bill_ids = AirwayBill.objects.all()
        
        self.fields['airway_bill_id'].choices = [(str(bill.id), str(bill)) for bill in self.airway_bill_ids]

    def clean(self):
        
        cleaned_data: dict = super().clean()
        airway_bill_id = cleaned_data.get('airway_bill_id')    

        if airway_bill_id:
            try:
                airway_bill_instance = self.airway_bill_ids.get(id=airway_bill_id)
                cleaned_data['airway_bill_id'] = airway_bill_instance
            except Service.DoesNotExist:
                # Handle the case where the Service instance with the given UUID doesn't exist
                raise forms.ValidationError("AirWayBill with the specified UUID does not exist.")
        
class GetBillingsLocationDetailsForm(forms.Form):
    airway_bill_id = forms.UUIDField(required=True)