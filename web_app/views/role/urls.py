from django.urls import path

from web_app.views.role import views

urlpatterns = [
    path("list/", views.ListRolesView.as_view(), name="list_roles"),
    path("json/list/", views.ListRoleInJsonFormat.as_view(), name="list_roles_json"),
    path("create/", views.CreateRoleView.as_view(), name="create_role"),
    path("specific/", views.GetSpecificRoleView.as_view(), name="get_specific_role"),
    path("update/", views.UpdateRoleView.as_view(), name="update_specific_role"),
    path("delete/", views.DeleteRoleView.as_view(), name="delete_specific_role"),
    path("check/name/", views.CheckRoleNameView.as_view(), name="check_role_name"),
]