# Create your views here.

from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.urls import reverse
from django.template.loader import render_to_string
from django.core import mail 
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import PasswordResetConfirmView


from web_app.models import AuthUser ,Department, Designation, Role, City
from web_app.forms import CreateAuthUserForm, UpdateAuthUserForm, GenerateUserActivationLinkAgainForm, CustomSetPasswordAndActivateForm
from web_app.utils import global_methods
from web_app.constants import *
# from web_app.core.view_base import BaseViewForAuthenticatedClass, BaseViewForAuthenticatedClassForJsonResponse


import os
import json
from inspect import currentframe, getframeinfo
from datetime import datetime
import traceback
import sys

import random
import string

INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"
frameinfo = getframeinfo(currentframe())
User = get_user_model()

# class ListAuthUserView(ListView,BaseViewForAuthenticatedClass):
class ListAuthUserView(ListView):
    template_name :str = 'users/list.html'
    model = AuthUser
    _page_title: str = "User"
    ordering: tuple = ("-created_at", )

    def _get_extra_context(self) -> dict:
        departments = Department.objects.filter(is_active=True, is_deleted=False).order_by("name")
        designations = Designation.objects.all()
        roles = Role.objects.filter(is_active=True, is_hidden=False).order_by('-created_at')
        # original_roles = OriginalRole.objects.filter(is_active=True,is_deleted=False).order_by('order')
        cities = City.objects.all()
        extra_context: dict = {
            "departments": departments,
            "designations": designations,
            "roles":roles,
            "cities":cities,
            # "original_roles":original_roles
        }
        return extra_context
    def get_queryset(self):
        qs = super().get_queryset()
        user= self.request.user
        username = user.username
        return qs.filter(is_admin=False,is_superuser=False).exclude(is_active=False,is_lock=False).exclude(username=username)

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        """ 
        extra_context: dict = self._get_extra_context()
        context.update({'page_title':self._page_title})
        context.update(extra_context)
        return super().render_to_response(context, **response_kwargs)
    
# class CreateAuthUser(BaseViewForAuthenticatedClassForJsonResponse):
class CreateAuthUser(View):

    token_generator = default_token_generator


    def _generate_activation_link(self, user):
        current_site = get_current_site(self.request)
        site_name = current_site.name
        protocol = "https" if self.request.is_secure() else "http"
        
        context = {
            "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": self.token_generator.make_token(user),
        }
        return protocol + "://" + site_name + str(reverse("activate_and_reset_password", kwargs=context))

    def post(self, request, *args, **kwargs):
        form_validation =  CreateAuthUserForm(data=request.POST)

        if form_validation.is_valid():

            # password = User.objects.make_random_password(length=10,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#')

            lowercase_letters = string.ascii_lowercase
            result_lower_letter = ''.join(random.choice(lowercase_letters) for i in range(3))
            uppercase_letters = string.ascii_uppercase
            result_uppercase_letters = ''.join(random.choice(uppercase_letters) for i in range(4))
            digits = string.digits
            result_digits = ''.join(random.choice(digits) for i in range(3))
            prunctuations = string.punctuation
            result_prunctuations = ''.join(random.choice(prunctuations) for i in range(3))



            password = result_lower_letter+result_digits+result_prunctuations+result_uppercase_letters
            inst = form_validation.save(commit=True)
            inst.set_password(password)
            inst.is_active = False
            inst.is_lock = True
            inst.save()
            activation_link:str = self._generate_activation_link(inst)
            global_methods.send_new_user_welcome_email(subject=NEW_USER_WELCOME_EMAIL_SUBJECT, to_email = inst.email , data={"full_name": inst.get_fullname, "username": inst.username, "activation_link": activation_link})

            self._generate_event_data_and_insert(line_num=frameinfo.lineno, password=password, inst=inst, success=True)
            self._generate_log_data_and_insert(inst=inst, success=True)
            return JsonResponse({"detail": f"AuthUser '{inst.username}' has been created successfully"}, status=200)
        
        self._generate_event_data_and_insert(line_num=frameinfo.lineno, success=False, errors=form_validation.errors)
        self._generate_log_data_and_insert(success=False)
        return JsonResponse(data={"detail": "Unable to create AuthUser", "errors": dict(form_validation.errors.items()), "errors_div": "create_"}, status=400)    