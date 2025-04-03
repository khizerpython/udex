from django.urls import path, include
from django.urls import path, register_converter
from django.urls.converters import UUIDConverter

register_converter(UUIDConverter, 'uuid')

from web_app.views.locations import views


urlpatterns = [
    path('billings_location/', views.ListAirwayBillLocationView.as_view(), name='list_airway_bill_locations'),
    path('billings_location/create', views.AirwayBillLocationView.as_view(), name='create_airway_bill_locations'),
    path('billings_location/details/', views.AirwayBillLocationDetailsView.as_view(), name='airway_bill_locations_details'),
    path('billings_location/delete/', views.AirwayBillLocationDeleteView.as_view(), name='delete_airway_bill_locations'),
    path("<uuid:bill_id>/", views.DownloadAirwayBillView.as_view(), name='download_airway_bill'),
    
    # path('update/billings/', views.UpdateAirwayBillView.as_view(), name='update_airway_bill'),
    # path('billings_details/', views.GetSpecificBillingDetails.as_view(), name='airway_bill_detail'),
    # path('billings/update', views.GetDataToUpdateSpecificBill.as_view(), name='get_specific_bill_to_update'),
    #  path("list/json/", views.ListOfAirwayBillsJsonFormat.as_view(), name="list_airway_bills_json"),
    
]