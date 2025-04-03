from django.urls import path, register_converter

from web_app.views.billings import views
from django.urls.converters import UUIDConverter

register_converter(UUIDConverter, 'uuid')


urlpatterns = [
    path('billings/', views.AirwayBillView.as_view(), name='airway_bill_list'),
    path('billings/create', views.CreateAirwayBillView.as_view(), name='airway_bill'),
    path('update/billings/', views.UpdateAirwayBillView.as_view(), name='update_airway_bill'),
    path('billings_details/', views.GetSpecificBillingDetails.as_view(), name='airway_bill_detail'),
    path('billings/update', views.GetDataToUpdateSpecificBill.as_view(), name='get_specific_bill_to_update'),
    path("list/json/", views.ListOfAirwayBillsJsonFormat.as_view(), name="list_airway_bills_json"),
    #  Label
    path("label/<uuid:bill_id>/", views.CreateAirwayBillLabelView.as_view(), name='create_airway_bill_label'),
    
]