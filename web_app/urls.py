from django.urls import path, include

urlpatterns = [
        path("", include("web_app.views.frontend.urls")),
        path("menu/", include("web_app.views.menu.urls")),
        path("users/", include("web_app.views.users.urls")),
        path("role/", include("web_app.views.role.urls")), 
        path("password/", include("web_app.views.reset_password.urls")),
        # path("dashboard/", include("bpm_webapp.views.dashboard.urls")),
        path("auth/", include("web_app.views.auth.urls")),
        path("", include("web_app.views.billings.urls")),
        path("", include("web_app.views.locations.urls")),
        # path("department/", include("bpm_webapp.views.department.urls")),
        # path("designation/", include("bpm_webapp.views.designation.urls")),
        # path("docs/", include("bpm_webapp.views.docs.urls")),
        # path("workflow/", include("bpm_webapp.views.workflows.urls")),
        # path("workflow/rights/assignment/", include("bpm_webapp.views.workflow_rights_assignment.urls")),
]

# handler404 = "bpm_webapp.views.404_view.views.page_not_found_view"