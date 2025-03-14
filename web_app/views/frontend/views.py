from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

# App level Import


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/homepage.html", {})


class DashboardPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "frontend/dashboard.html", {})
