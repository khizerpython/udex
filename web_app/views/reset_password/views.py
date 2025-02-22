from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

from web_app.forms import CustomResetPasswordForm


class CustomPasswordResetView(PasswordResetView):

    email_template_name = "email_templates/generic_notification.html"
    extra_email_context = {}
    form_class = CustomResetPasswordForm
    success_url = reverse_lazy("reset_done_password")
    template_name = "reset_password/reset_pass_form.html"

    # Inheriting this to pass request object to `CustomResetPasswordForm` to access it while sending email to fetch the user ip. 
    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            "initial": self.get_initial(),
            "prefix": self.get_prefix(),
            "request": self.request
        }

        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "data": self.request.POST,
                    "files": self.request.FILES,
                }
            )
        return kwargs

class CustomPasswordResetConfirmView(PasswordResetConfirmView):

    post_reset_login = False
    post_reset_login_backend = None
    success_url = reverse_lazy("password_reset_done")
    template_name = "reset_password/password_reset_done.html"

