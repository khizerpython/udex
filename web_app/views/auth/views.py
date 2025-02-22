from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect

from web_app.forms import CustomAuthenticationForm
from web_app.utils.global_methods import get_client_ip
from web_app import constants

import os


class CustomLoginView(LoginView):
    template_name="auth/login.html"
    form_class=CustomAuthenticationForm
    extra_context = {"title": "UDEX Login"}
    redirect_authenticated_user= True # So users can't be able to access Login Page after login


    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        self.request.session["client_ip"] = get_client_ip(self.request)
        self.request.session.save()
        user = form.get_user()
        self.request.session['is_first_login'] = user.is_first_login
        # Setting is_first_login False if True. True was set automatically when user was created, which means that the user has not logged-in to the portal yet.   
        if user.is_first_login:
            
            user.is_first_login = False # Means that the user has done with first login, now the value is False means he is using portal
            user.save()
        return HttpResponseRedirect(self.get_success_url())


class CustomLogoutView(LogoutView):


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
