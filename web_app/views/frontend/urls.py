from django.urls import path

from web_app.views.frontend import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage_view"),
    path('dashboard/',views.DashboardPageView.as_view(),name='dashboard_view'),
    # path('countdowntimer/',views.CountDownTimer.as_view(),name='countdowntimer'),
    # path('modaltesting/',views.ModelTesting.as_view(),name='modal_testing'),
    
]