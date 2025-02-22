from django.urls import path

from web_app.views.auth import views


urlpatterns = [   
    path("login/", views.CustomLoginView.as_view(), name="login_url"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout_url"),
]