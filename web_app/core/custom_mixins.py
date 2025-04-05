from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import logout_then_login
from django.urls import resolve
from django.shortcuts import resolve_url
from django.http.response import JsonResponse
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser

from web_app.models import Menus
from web_app.constants import ADMIN_EMAIL_ADDRESS
from web_app.utils.global_methods import  send_session_out_request_email

# Third party imports
from urllib.parse import urlparse
import os

def insert_no_permission_event(request):
    
    subject = "Unauthorized User"
    to_email= ADMIN_EMAIL_ADDRESS
    send_session_out_request_email(subject=subject, to_email=to_email, request=request)



class CustomLoginAndMenuValidatorMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        """
        Overriding to restrict users to access non-assigned menus after login.
        """
        url_name = resolve(self.request.path_info).url_name
        # if url_name == "dashboard" and not self.request.user.role_id.menu_ids.filter(url=url_name).exists():
        #     Session.objects.get(session_key=self.request.session.session_key).delete()
        
        # Check if parent menu is active or not. If in-active return False 
        parent_menu = Menus.objects.get(url=url_name).parent_id
        if parent_menu is not None:
            if not parent_menu.is_active:
                return False

        try:
            self.request.user.role_id.menu_ids.get(url=url_name)
            return True
        except ObjectDoesNotExist as e:
            try:
                menu_obj = Menus.objects.get(url=url_name)
                self.request.user.role_id.menu_ids.get(url=menu_obj.inner_menu_of.url)
                return True
            except ObjectDoesNotExist as e:
                return False
            except AttributeError:
                return False
        except AttributeError:
            return False

    def handle_no_permission(self):
        """
        Overriding to control `403 forbidden` error
        """

        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())

        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        
        insert_no_permission_event(self.request)
        return logout_then_login(self.request, resolved_login_url)


class CustomLoginAndMenuValidatorMixinForJsonResponseView(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        """
        Overriding to restrict users to access non-assigned menus after login.
        """
        url_name = resolve(self.request.path_info).url_name
        # if url_name == "dashboard" and not self.request.user.role_id.menu_ids.filter(url=url_name).exists():
        #     Session.objects.get(session_key=self.request.session.session_key).delete()
        try:
            self.request.user.role_id.menu_ids.get(url=url_name)
            return True
        except ObjectDoesNotExist as e:
            # try:
            #     menu_obj = Menus.objects.get(url=url_name)
            #     self.request.user.role_id.menu_ids.get(url=menu_obj.inner_menu_of.url)
            #     return True
            # except ObjectDoesNotExist as e:
                return False
        except AttributeError:
            return False

    def handle_no_permission(self):
        """
        Overriding to control `403 forbidden` error
        """

        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())

        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()

        insert_no_permission_event(self.request)
        return JsonResponse(
            {
                "path": path,
                "redirect_url": reverse("logout_url")
            },
            status=401
        )