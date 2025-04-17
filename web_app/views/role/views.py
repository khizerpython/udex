from django.views.generic import ListView
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.urls import reverse
from django.db.models import Q

from web_app.models import Role, Department, Menus, AuthUser
from web_app.forms import RoleForm, UpdateRoleForm, RIGHTS_CATEGORY_DICT, RIGHTS_AUTHENTICATION_FRONTEND
from web_app.core.view_base import BaseViewForAuthenticatedClass, BaseViewForAuthenticatedClassForJsonResponse
from web_app.constants import *
from django.views import View
import json
from inspect import currentframe, getframeinfo
from datetime import datetime

frameinfo = getframeinfo(currentframe())


class ListRolesView(ListView, BaseViewForAuthenticatedClass):
# class ListRolesView(ListView):
    template_name: str = "role/list.html"
    model = Role
    _page_title = "Rights & Menu Assignment"
    ordering: tuple = ("-created_at", )

    def _get_extra_context(self) -> dict:
        departments = Department.objects.filter(is_active=True, is_deleted=False).order_by("name")
        menus = Menus.objects.filter(is_active=True).order_by("-created_at")

        extra_context: dict = {
            "departments": departments,
            "menus": menus,
            'rights_categories':RIGHTS_CATEGORY_DICT,
            'rights_authentication_frontend' :RIGHTS_AUTHENTICATION_FRONTEND
        }
        return extra_context

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        """
        extra_context: dict = self._get_extra_context()
        context.update({"page_title": self._page_title})
        context.update(extra_context)
        return super().render_to_response(context, **response_kwargs)

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()
        return qs.filter(is_hidden=False)


class CreateRoleView(BaseViewForAuthenticatedClassForJsonResponse):
# class CreateRoleView(View):


    def post(self, request, *args, **kwargs):
        form_validation = RoleForm(data=request.POST)

        if form_validation.is_valid():
            inst = form_validation.save()
            inst.save()
            
            return JsonResponse({"detail": f"Role '{inst.name}' has been created successfully"}, status=200)
        
        return JsonResponse(data={"detail": "Unable to create role", "errors":dict(form_validation.errors.items()), "errors_div": "create_"}, status=400)


class ListRoleInJsonFormat(BaseViewForAuthenticatedClassForJsonResponse):
# class ListRoleInJsonFormat(View):

    def _merge_objects(self, data: QuerySet) -> dict:
        return_data: dict = {}

        def merge_objects(obj_id, obj):
            stored_obj: dict = return_data.get(obj_id, {})

            for key, value in obj.items():
                stored_obj_value = stored_obj.get(key)
                if isinstance(stored_obj_value, str):
                    if isinstance(value, datetime):
                        # value = timezone.localtime(value).strftime(DATE_TIME_FORMAT)
                        value = value.strftime(DATE_TIME_FORMAT)
                    if stored_obj_value != value:
                        return_data[obj_id][key] = [stored_obj_value, value]
                elif isinstance(stored_obj_value, datetime):
                    # return_data[obj_id][key] = timezone.localtime(stored_obj_value).strftime(DATE_TIME_FORMAT)
                    return_data[obj_id][key] = stored_obj_value.strftime(DATE_TIME_FORMAT)
                elif isinstance(stored_obj_value, list):
                    if value not in return_data[obj_id][key]:
                        return_data[obj_id][key].append(value)

        def iterate_object(obj_id: str):
            
            for key, value in return_data.get(obj_id, {}).items():
                if isinstance(value, datetime):
                    # return_data[obj_id][key] = timezone.localtime(value).strftime(DATE_TIME_FORMAT)
                    return_data[obj_id][key] = value.strftime(DATE_TIME_FORMAT)
                    
            return_data[obj_id]["specific_url"] = reverse("get_specific_role")
            return_data[obj_id]["delete_url"] = reverse("delete_specific_role")

        for obj in data:
            obj_id: str = str(obj.pop("id", ""))
            if obj_id not in return_data:
                return_data[obj_id] = obj
                iterate_object(obj_id)
            else:
                merge_objects(obj_id, obj)

        return return_data

    def get(self, request, *args, **kwargs):
        roles = Role.objects.select_related().filter(is_hidden=False).order_by("-created_at").values("id", "name", "order", "is_active", "menu_ids__name", "updated_at")
        roles_dict: dict = self._merge_objects(roles)
        return JsonResponse(data=roles_dict, status=200)


class GetSpecificRoleView(BaseViewForAuthenticatedClassForJsonResponse):


    def _get(self, request, *args, **kwargs):
        role_id: str = request.POST.get("object_uuid")
        try:
            role_obj = Role.objects.filter(id=role_id, is_hidden=False)
        except ValidationError:
            return JsonResponse({"detail": "Invalid object ID"}, status=400)

        if not role_obj.first():
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
        serialized_obj: dict = json.loads(serializers.serialize(format="json", queryset=role_obj))
        return JsonResponse(data=serialized_obj[0].get("fields", {}), status=200, safe=False)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)
    

class UpdateRoleView(BaseViewForAuthenticatedClassForJsonResponse):
# class UpdateRoleView(View):

    def post(self, request, *args, **kwargs):
        try:
            inst = Role.objects.get(id=request.POST.get("hidden_id", None), is_hidden=False)
        except Role.DoesNotExist:
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
         
        validation_form = UpdateRoleForm(data=request.POST, instance=inst)

        if validation_form.is_valid():
            form_inst = validation_form.save(commit=False)
            # Check if role is assign to any user ,So we can validate
            if not form_inst.is_active:
                users_count_with_requested_role:int = AuthUser.objects.filter(role_id=inst).count()
                if users_count_with_requested_role > 0:
                    return JsonResponse({"detail": f"Can't inactive {inst.name}. Please unassigned {inst.name} from Users to inactive."}, status=400)
            form_inst.save()
            validation_form.save_m2m()
            form_inst.menu_ids.add(DASHBOARD)
            # form_inst.menu_ids.add(DOCS)
            form_inst.save()
               
            return JsonResponse({"detail": f"{inst.name} has been updated successfully"}, status=200)
        
        return JsonResponse({"detail": f"Unable to perform update operation on {inst.name}", "errors": validation_form.errors, "errors_div": "edit_"}, status=400)


class DeleteRoleView(BaseViewForAuthenticatedClassForJsonResponse):
# class DeleteRoleView(View):

    def post(self, request, *args, **kwargs):
        try:
            inst = Role.objects.get(id=request.POST.get("id", None), is_hidden=False)
        except Role.DoesNotExist:
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
        users_count_with_requested_role:int = AuthUser.objects.filter(role_id=inst).count()
        if users_count_with_requested_role > 0:
            return JsonResponse({"detail": f"Can't delete {inst.name}. Please unassigned {inst.name} from Users to delete."}, status=400)
        
    
        log_inst_name = inst.name # Saving instance name for event and logs
        inst.delete()
        return JsonResponse({"detail": f"{inst.name} has been deleted successfully"}, status=200)


class CheckRoleNameView(BaseViewForAuthenticatedClassForJsonResponse):
# class CheckRoleNameView(View):

    def _get(self, request , *args, **kwargs):
        name = request.POST.get('name')
        object_id = request.POST.get('object_id')
        query = Q(name=name)
        if object_id:
            query = query & ~Q(id=object_id)
        try:
            Role.objects.get(query)
            return JsonResponse({"exists": True},status=400)
        except Role.DoesNotExist:
            return JsonResponse({"exists": False},status=200)

    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)


