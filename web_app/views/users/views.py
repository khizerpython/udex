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
from web_app.core.view_base import BaseViewForAuthenticatedClass, BaseViewForAuthenticatedClassForJsonResponse


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

class ListAuthUserView(ListView,BaseViewForAuthenticatedClass):
# class ListAuthUserView(ListView):
    template_name :str = 'users/list.html'
    model = AuthUser
    _page_title: str = "User"
    ordering: tuple = ("-created_at", )

    def _get_extra_context(self) -> dict:
        departments = Department.objects.filter(is_active=True, is_deleted=False).order_by("name")
        designations = Designation.objects.all()
        roles = Role.objects.filter(is_active=True, is_hidden=False).order_by('-created_at')
        cities = City.objects.all()
        extra_context: dict = {
            "departments": departments,
            "designations": designations,
            "roles":roles,
            "cities":cities,
        }
        return extra_context
    def get_queryset(self):
        qs = super().get_queryset()
        
        return qs.filter(is_admin=False,is_superuser=False).exclude(is_active=False,is_lock=False)

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
    
class CreateAuthUser(BaseViewForAuthenticatedClassForJsonResponse):
# class CreateAuthUser(View):

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

            return JsonResponse({"detail": f"AuthUser '{inst.username}' has been created successfully"}, status=200)
        
        return JsonResponse(data={"detail": "Unable to create AuthUser", "errors": dict(form_validation.errors.items()), "errors_div": "create_"}, status=400)   

class DeleteAuthUserView(BaseViewForAuthenticatedClassForJsonResponse):
# class DeleteAuthUserView(View):

    def all_unexpired_sessions_for_user(self, user):
        user_sessions = []
        all_sessions  = Session.objects.all()
        for session in all_sessions:
            session_data = session.get_decoded()
            if user.pk == session_data.get('_auth_user_id'):
                user_sessions.append(session.pk)
        return Session.objects.filter(pk__in=user_sessions)

    def delete_all_unexpired_sessions_for_user(self, user, session_to_omit=None):
        session_list = self.all_unexpired_sessions_for_user(user)
        if session_to_omit is not None:
            session_list.exclude(session_key=session_to_omit.session_key)
        session_list.delete()

    def post(self, request, *args, **kwargs):
        try:
            inst = AuthUser.objects.get(id=request.POST.get("id", None))
        except AuthUser.DoesNotExist:
            
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
        inst.is_active = False
        inst.is_lock = False
        inst.last_login = timezone.now()
        inst.save()
        self.delete_all_unexpired_sessions_for_user(inst) # Deleting user session

        return JsonResponse({"detail": f"{inst.username} has been deleted successfully"}, status=200)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class=CustomSetPasswordAndActivateForm
    title = "Account Activation"
    post_reset_login = False
    template_name='users/user_activation_and_reset_password.html'

    def form_valid(self, form):
        _ = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        return render(self.request, self.template_name, {"reset_done": True, "title": "Account Activated"})


class CheckAuthUserNameView(BaseViewForAuthenticatedClassForJsonResponse):
# class CheckAuthUserNameView(View):


    def _get(self, request , *args, **kwargs):
        name = request.POST.get('name')
       
        try:
            AuthUser.objects.get(username=name)
            return JsonResponse({"exists": True},status=400)
        except AuthUser.DoesNotExist:
            return JsonResponse({"exists": False},status=200)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)     
    
class CheckUpdatEmailView(BaseViewForAuthenticatedClassForJsonResponse):
# class CheckUpdatEmailView(View):


    def _get(self, request , *args, **kwargs):
        email = request.POST.get('email')
        id = request.POST.get('id')
        try:
            AuthUser.objects.exclude(id=id).get(email=email)
            return JsonResponse({"exists": True},status=400)
        except AuthUser.DoesNotExist:
            return JsonResponse({"exists": False},status=200)

    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)   


class CheckEmailAddress(BaseViewForAuthenticatedClassForJsonResponse):
# class CheckEmailAddress(View):

    def _get(self, request , *args, **kwargs):
        email = request.POST.get('email')
        try:
            AuthUser.objects.get(email=email)
            return JsonResponse({"exists": True},status=400)
        except AuthUser.DoesNotExist:
            return JsonResponse({"exists": False},status=200)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)  


class GetDesignationOfDepartment(BaseViewForAuthenticatedClassForJsonResponse):
# class GetDesignationOfDepartment(View):


    def _get(self, request , *args, **kwargs):
        depart_id = request.POST.get('depart_id')
        try:
            designations_of_departs = Designation.objects.filter(is_active=True,department_id__in=depart_id)

            serialized_obj: dict = json.loads(serializers.serialize(format="json", queryset=designations_of_departs))
            return JsonResponse(data=serialized_obj,status=200,safe=False)
        except Designation.DoesNotExist:
            return JsonResponse({"exists": False},status=400)



    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)     

class GenerateUserActivationLinkAgainJsonView(CreateAuthUser):

    def post(self, request, *args, **kwargs):
        
        form_validation =  GenerateUserActivationLinkAgainForm(data=request.POST)

        if form_validation.is_valid():
            inst = form_validation.cleaned_data.get("inst_id")
            activation_link:str = self._generate_activation_link(inst)
            global_methods.send_new_user_welcome_email(subject=NEW_USER_WELCOME_EMAIL_SUBJECT, to_email = inst.email , data={"full_name": inst.get_fullname, "username": inst.username, "activation_link": activation_link})

            return JsonResponse({"detail": "Activation link sent sucessfully"}, status=200)
        
        return JsonResponse(data={"detail": "Unable to generate link. Invalid object ID", "redirect_url": reverse("logout_url")}, status=401)


class ListAuthUserInJsonFormat(BaseViewForAuthenticatedClassForJsonResponse):
# class ListAuthUserInJsonFormat(View):

    def _merge_objects(self, data: list, authusers_querset) -> dict:
        return_data: dict = {}

        def iterate_object(obj_id: str):
            queryset_inst = authusers_querset.get(id=obj_id)
            for key, value in return_data.get(obj_id, {}).items():
                if key == "created_at":
                    obj_date_time = queryset_inst.created_at
                    return_data[obj_id][key] = obj_date_time.strftime(DATE_TIME_FORMAT)
                if key == "designation_id":
                    if value is not None:
                        designation = Designation.objects.get(id = value)
                        return_data[obj_id][key] = designation.name
                    else:
                        return_data[obj_id][key] = None


            return_data[obj_id]["show_resend_activation_link_button"] = queryset_inst.show_resend_activation_link_button
            return_data[obj_id]["specific_url"] = reverse("get_specific_user")
            return_data[obj_id]["delete_url"] = reverse("delete_specific_user")
            return_data[obj_id]["regenerate_url"] = reverse("generate_new_activiation_link")           

        for obj_from_list in data:
            obj_id: str = obj_from_list.get("pk", "")
            if obj_id not in return_data:
                return_data[obj_id] = obj_from_list.get("fields", {})
                iterate_object(obj_id)

        return return_data


    def get(self, request, *args, **kwargs):
        user = self.request.user
        username = user.username
        authusers = AuthUser.objects.select_related().filter(is_admin=False,is_superuser=False).exclude(is_active=False,is_lock=False).exclude(username=username).order_by("-created_at").only("id", "username","email", "designation_id", "is_active","is_lock", "created_at", "updated_at")
        serialize_authusers: list = json.loads(serializers.serialize("json", queryset=authusers, fields=("id", "username","email", "designation_id", "is_active","is_lock", "created_at", "updated_at")))
        authusers_dict: dict = self._merge_objects(serialize_authusers, authusers)
        return JsonResponse(data=authusers_dict, status=200)   

class GetSpecificAuthUserView(BaseViewForAuthenticatedClassForJsonResponse):
# class GetSpecificAuthUserView(View):

    def _get(self, request, *args, **kwargs):
        authuser_id: str = request.POST.get("object_uuid")
        try:
            authuser_obj = AuthUser.objects.filter(id=authuser_id)   
        except ValidationError:
            return JsonResponse({"detail": "Invalid object ID"}, status=400)

        if not authuser_obj.first():
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
        serialized_obj: dict = json.loads(serializers.serialize(format="json", queryset=authuser_obj))
        for roles in authuser_obj:
            role_id = roles.role_id
        
        data={
            'obj': serialized_obj[0].get("fields", {}),
            'id': serialized_obj[0].get("pk", {}),
            'name':role_id.name,
            'is_hod_right':role_id.is_hod_right
            
        }
        return JsonResponse(data=data, status=200, safe=False)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)  


class UpdateAuthUserView(BaseViewForAuthenticatedClassForJsonResponse):
# class UpdateAuthUserView(View):

    def all_unexpired_sessions_for_user(self, user):
        user_sessions = []
        all_sessions  = Session.objects.all()
        for session in all_sessions:
            session_data = session.get_decoded()
            if user.pk == session_data.get('_auth_user_id'):
                user_sessions.append(session.pk)
        return Session.objects.filter(pk__in=user_sessions)

    def delete_all_unexpired_sessions_for_user(self, user, session_to_omit=None):
        session_list = self.all_unexpired_sessions_for_user(user)
        if session_to_omit is not None:
            session_list.exclude(session_key=session_to_omit.session_key)
        session_list.delete()

    def post(self, request, *args, **kwargs):
        
        try:
            inst = AuthUser.objects.get(id=request.POST.get("hidden_id", None))
        except AuthUser.DoesNotExist:
            
            return JsonResponse({"detail": "Invalid object ID"}, status=400)

        validation_form = UpdateAuthUserForm(data=request.POST, instance=inst)

        if validation_form.is_valid(): 
            id = request.POST.get('hidden_id')
            
            inst = validation_form.save()
            user = AuthUser.objects.get(id=id)
            if user.is_lock == True:
                user.is_active = False
                self.delete_all_unexpired_sessions_for_user(user)
            else:
                user.is_active = True
            user.save()        

            return JsonResponse({"detail": f"{inst.username} has been updated successfully"}, status=200)
        
        return JsonResponse({"detail": f"Unable to perform update operation on {inst.username}", "errors": dict(validation_form.errors.items()), "errors_div": "edit_"}, status=400)
