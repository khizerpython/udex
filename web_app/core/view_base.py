from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http.response import JsonResponse

from web_app.core.custom_mixins import CustomLoginAndMenuValidatorMixin, CustomLoginAndMenuValidatorMixinForJsonResponseView

decorators = [never_cache, login_required]


@method_decorator(decorators, name='dispatch')
class BaseViewForAuthenticatedClass(CustomLoginAndMenuValidatorMixin, View):
    
    def get(self, request, *args, **kwargs):
        raise NotImplementedError("get method not implemented.")
    
    def post(self, request, *args, **kwargs):
        raise NotImplementedError("post method not implemented.")
    
    def put(self, request, *args, **kwargs):
        raise NotImplementedError("put method not implemented.")
    
    def patch(self, request, *args, **kwargs):
        raise NotImplementedError("patch method not implemented.")
    
    def delete(self, request, *args, **kwargs):
        raise NotImplementedError("delete method not implemented.")


class BaseViewForAuthenticatedClassForJsonResponse(CustomLoginAndMenuValidatorMixinForJsonResponseView, View):
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "detail": "get method not implemented.",
                "redirect_url": reverse("logout_url")
            },
            status=501
        )
    
    def post(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "detail": "post method not implemented.",
                "redirect_url": reverse("logout_url")
            },
            status=501
        )
    
    def put(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "detail": "put method not implemented.",
                "redirect_url": reverse("logout_url")
            },
            status=501
        )
    
    def patch(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "detail": "patch method not implemented.",
                "redirect_url": reverse("logout_url")
            },
            status=501
        )
    
    def delete(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "detail": "delete method not implemented.",
                "redirect_url": reverse("logout_url")
            },
            status=501
        )