from web_app.models import Menus

from django.urls import resolve
from itertools import chain
from django.db.models import Case, When
from web_app.constants import *

def get_side_menus(request):
    if not request.user.is_anonymous:
        objs = request.user.role_id.menu_ids.annotate(merged_order=Case(When(parent_id__isnull=True, then="order"), default="parent_id__order")).filter(is_active=True, inner_menu_of__isnull=True).order_by("merged_order", "parent_id__name").values("name", "url", "parent_id__is_active", "parent_id__name", "order", "parent_id__order", "merged_order")
        if request.user.is_user_is:
            my_objs = [d for d in objs if d['url'] != 'list_workflow_participated_report']
        else:
            my_objs = [d for d in objs if d['url'] != 'list_workflow_report']
        return my_objs
        # return request.user.role_id.menu_ids.annotate(merged_order=Case(When(parent_id__isnull=True, then="order"), default="parent_id__order")).filter(is_active=True, inner_menu_of__isnull=True).order_by("merged_order", "parent_id__name").values("name", "url", "parent_id__is_active", "parent_id__name", "order", "parent_id__order", "merged_order")
    return []

def get_selected_side_menu(request):
    url_name = resolve(request.path_info).url_name
    return url_name

def get_selected_side_menu_parent_name(url_name):
    try:
        parent_name = Menus.objects.get(url=url_name).parent_id.name
    except (Menus.DoesNotExist, AttributeError):
        parent_name = None
    return parent_name



def side_menus_context_processor(request):
    """
    Return a lazy 'side_menus' context variable for the allowed 
    """
    user = request.user
    if user.is_authenticated:

        selected_menu_url_name:str = get_selected_side_menu(request)
        return {
            "side_menus": get_side_menus(request),
            "selected_menu": selected_menu_url_name,
            "parent_menu": get_selected_side_menu_parent_name(selected_menu_url_name),
            "ENCRYPTION_DECRYPTION_PASSWORD":ENCRYPTION_DECRYPTION_PASSWORD
        }




