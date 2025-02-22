from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from web_app.views.reset_password import views
from web_app.forms import CustomSetPasswordForm

urlpatterns = [
    path("reset/", views.CustomPasswordResetView.as_view(), name="reset_password"),
    path("done/", auth_views.PasswordResetDoneView.as_view(
        template_name = "reset_password/email_send_msg.html"
    ), name="reset_done_password"),
    path('change/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm, success_url = reverse_lazy("password_reset_done"), template_name='reset_password/confirm_email.html'), name='password_reset_confirm'),
    path("", auth_views.PasswordResetCompleteView.as_view(template_name = "reset_password/password_reset_done.html"), name="password_reset_done"),
]
