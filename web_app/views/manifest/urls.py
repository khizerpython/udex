from django.urls import path

from web_app.views.manifest import views

urlpatterns = [   
    path('list/',views.ListManifestView.as_view(),name='menifest_list'),
    path('get/manifest/',views.GetManifestView.as_view(),name='get_menifest_data'),
    path('make/airway/bill/manifest/',views.AirwayBillManifestCheckedView.as_view(),name='make_airway_bill_manifest'),
    
]