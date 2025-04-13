from django.urls import path

from web_app.views.frontend import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage_view"),
    path('dashboard/',views.DashboardPageView.as_view(),name='dashboard_view'),
    path('aboutus/',views.AboutUsPageView.as_view(),name='about_us_view'),
    path('contactus/',views.ContactUsPageView.as_view(),name='contact_us_view'),
    # Tracking page
    path('location/', views.LocationView.as_view(), name='location_page'),
    # path('countdowntimer/',views.CountDownTimer.as_view(),name='countdowntimer'),
    # path('modaltesting/',views.ModelTesting.as_view(),name='modal_testing'),
    
]