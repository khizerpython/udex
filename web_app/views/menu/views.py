from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.urls import reverse
from django.template.loader import render_to_string
from django.core import mail
from web_app.models import Menus
from web_app.forms import CreateMenusForm,UpdateMenusForm
from web_app.constants import *
from web_app.core.view_base import BaseViewForAuthenticatedClass, BaseViewForAuthenticatedClassForJsonResponse

import os
import json
from inspect import currentframe, getframeinfo
from datetime import datetime
import traceback
import sys

frameinfo = getframeinfo(currentframe())



class ListMenuView(ListView,BaseViewForAuthenticatedClass):
# class ListMenuView(ListView):
    template_name :str = 'menu/list.html'
    model = Menus
    _page_title: str = "Menu"
    ordering: tuple = ("-created_at", )

    def _get_extra_context(self) -> dict:
        parent_menus = Menus.objects.filter(parent_id__isnull=True)
        all_menus = Menus.objects.all()
        extra_context: dict = {
            
            "menus": parent_menus,
            "all_menus": all_menus,
        }
        return extra_context
    

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


class CreateMenu(BaseViewForAuthenticatedClassForJsonResponse):
# class CreateMenu(View):
    """
    This class has two method:
    GET : method took all the designation, from database and show them on template datatable.
    POST : method check if the values in designation are correct or not , if correct, post them to database, and show them to the template 
    """
    def _merge_objects(self, data: list) -> dict:
        return_data: dict = {}

        def iterate_object(obj_id: str):
            
            for key, value in return_data.get(obj_id, {}).items():
                # if key == "created_at":
                #     return_data[obj_id][key] = timezone.make_aware(datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ'), timezone.get_current_timezone(), True).strftime(DATE_TIME_FORMAT)
                if key == "name":
                        return_data[obj_id]=value    
                    
           

        for obj_from_list in data:
            obj_id: str = obj_from_list.get("pk", "")
            if obj_id not in return_data:
                return_data[obj_id] = obj_from_list.get("fields", {})
                iterate_object(obj_id)

        return return_data


    def _get_menus(self) -> dict:
        menus = Menus.objects.filter(parent_id__isnull=True)
        return menus  

    def _get_inner_menus(self) -> dict:
        inner_menus = Menus.objects.all()
        return inner_menus      

    def post(self, request, *args, **kwargs):

        form_validation =  CreateMenusForm(data=request.POST)

        if form_validation.is_valid():
            inst = form_validation.save()
            extra_context = self._get_menus()
            inner_menus = self._get_inner_menus()
            menu: list = json.loads(serializers.serialize("json", queryset=extra_context))
            inner_menu_list: list = json.loads(serializers.serialize("json", queryset=inner_menus))
            
            menu_dict: dict = self._merge_objects(menu)
            inner_menu_dict: dict = self._merge_objects(inner_menu_list)
            return JsonResponse({"detail": f"Menu '{inst.name}' has been created successfully", "menu_dict": menu_dict, "inner_menu_dict":inner_menu_dict}, status=200)
        
        self._generate_log_data_and_insert(success=False)
        return JsonResponse(data={"detail": "Unable to create menu", "errors": dict(form_validation.errors.items()), "errors_div": "create_"}, status=400)      


class ListMenuInJsonFormat(BaseViewForAuthenticatedClassForJsonResponse):
# class ListMenuInJsonFormat(View):
    
    def _merge_objects(self, data: QuerySet) -> dict:
        return_data: dict = {}

        def merge_objects(obj_id, obj):
            stored_obj: dict = return_data.get(obj_id, {})

            for key, value in obj.items():
                stored_obj_value = stored_obj.get(key)
                if isinstance(stored_obj_value, str):
                    if isinstance(value, datetime):
                        value = value.strftime(DATE_TIME_FORMAT)
                    if stored_obj_value != value:
                        return_data[obj_id][key] = [stored_obj_value, value]
                elif isinstance(stored_obj_value, datetime):
                    return_data[obj_id][key] = stored_obj_value.strftime(DATE_TIME_FORMAT)
                elif isinstance(stored_obj_value, list):
                    if value not in return_data[obj_id][key]:
                        return_data[obj_id][key].append(value)

        def iterate_object(obj_id: str):
            
            for key, value in return_data.get(obj_id, {}).items():
                if isinstance(value, datetime):
                    # return_data[obj_id][key] = timezone.localtime(value, timezone.get_default_timezone()).strftime(DATE_TIME_FORMAT)
                    return_data[obj_id][key] = value.strftime(DATE_TIME_FORMAT)
                    # return_data[obj_id][key] = value.strftime(DATE_TIME_FORMAT)
            return_data[obj_id]["specific_url"] = reverse("get_specific_menu")
            return_data[obj_id]["delete_url"] = reverse("delete_specific_menu")

        for obj in data:
            obj_id: str = str(obj.pop("id", ""))
            if obj_id not in return_data:
                return_data[obj_id] = obj
                iterate_object(obj_id)
            else:
                merge_objects(obj_id, obj)

        return return_data

    def get(self, request, *args, **kwargs):
        menus = Menus.objects.select_related().order_by("-created_at").values("id", "name","url","is_active", "updated_at", "parent_id__name")
        menu_dict: dict = self._merge_objects(menus)
        return JsonResponse(data=menu_dict, status=200)    


class GetSpecificMenuView(BaseViewForAuthenticatedClassForJsonResponse):
# class GetSpecificMenuView(View):

    
    def _get(self, request, *args, **kwargs):
        menu_id: str = request.POST.get("object_uuid")
        
        try:
            menu_obj = Menus.objects.filter(id=menu_id)

        except ValidationError:
            return JsonResponse({"detail": "Invalid object ID"}, status=400)

        if not menu_obj.first():
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
        
        parent_serialized_obj: dict = json.loads(serializers.serialize(format="json", queryset=menu_obj))
        data = {
            'parent_serialized_obj':parent_serialized_obj[0].get("fields", {}),
            'id': parent_serialized_obj[0].get("pk", {}),
        }
        return JsonResponse(data=data, status=200, safe=False)

    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)    


class UpdateMenuView(BaseViewForAuthenticatedClassForJsonResponse):
# class UpdateMenuView(View):

    def _merge_objects(self, data: list) -> dict:
        return_data: dict = {}

        def iterate_object(obj_id: str):
            
            for key, value in return_data.get(obj_id, {}).items():
                if key == "name":
                        return_data[obj_id]=value     
           

        for obj_from_list in data:
            obj_id: str = obj_from_list.get("pk", "")
            if obj_id not in return_data:
                return_data[obj_id] = obj_from_list.get("fields", {})
                iterate_object(obj_id)

        return return_data

    def _get_menus(self) -> dict:
        menus = Menus.objects.filter(parent_id__isnull=True)
        return menus 

    def _get_inner_menus(self) -> dict:
        inner_menus = Menus.objects.all()
        return inner_menus       

    def post(self, request, *args, **kwargs):
        try:
            inst = Menus.objects.get(id=request.POST.get("hidden_id", None))
        except Menus.DoesNotExist:
            
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
         
        validation_form = UpdateMenusForm(data=request.POST, instance=inst)

        if validation_form.is_valid(): 
            validation_form.save()
            
            extra_context = self._get_menus()
            inner_menus = self._get_inner_menus()
            menu: list = json.loads(serializers.serialize("json", queryset=extra_context))
            inner_menu_list: list = json.loads(serializers.serialize("json", queryset=inner_menus))
            menu_dict: dict = self._merge_objects(menu)
            inner_menu_dict: dict = self._merge_objects(inner_menu_list)
            return JsonResponse({"detail": f"{inst.name} has been updated successfully", "menu_dict": menu_dict, "inner_menu_dict":inner_menu_dict}, status=200)
  
        
        
        return JsonResponse({"detail": f"Unable to perform update operation on {inst.name}", "errors": dict(validation_form.errors.items()), "errors_div": "edit_"}, status=400)


class DeleteMenuView(BaseViewForAuthenticatedClassForJsonResponse):
# class DeleteMenuView(View): 

    def post(self, request, *args, **kwargs):
        try:
            inst = Menus.objects.get(id=request.POST.get("id", None))
        except Menus.DoesNotExist:
           
            return JsonResponse({"detail": "Invalid object ID"}, status=400)
        log_inst_name = inst.name # Saving instance name for event and logs
        inst.delete()
        return JsonResponse({"detail": f"{inst.name} has been deleted successfully"}, status=200)


class CheckMenusNameView(View):


    def _get(self, request , *args, **kwargs):
        name = request.POST.get('name')
       
        try:
            Menus.objects.get(name=name)
            return JsonResponse({"exists": True},status=400)
        except Menus.DoesNotExist:
            return JsonResponse({"exists": False},status=200)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)


class CheckUpdateMenusNameView(View):
    

    def _get(self, request , *args, **kwargs):
        name = request.POST.get('name')
        id = request.POST.get('id')
        try:
            Menus.objects.exclude(id=id).get(name=name)
            return JsonResponse({"exists": True},status=400)
        except Menus.DoesNotExist:
            return JsonResponse({"exists": False},status=200)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)  


class GetChildMenus(View):
    def _get(self, request , *args, **kwargs):
        id = request.POST.get('id')
        try:
            child_menus = Menus.objects.filter(parent_id=id).only("name")
            serilized_child_array = json.loads(serializers.serialize(format="json", queryset=child_menus))
            child_dict = []
            for fields in serilized_child_array:
                child_dict.append(fields["fields"])
            
            data = {
                "child_menus":child_dict
                }
            return JsonResponse(data=data,status=200)
        except:  
            data = {
                "child_menus":"no child menus"
            }
            return JsonResponse(data=data,status=400)

    
    def post(self, request, *args, **kwargs):
        return self._get(request, *args, **kwargs)     