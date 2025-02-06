from django.urls import path, reverse_lazy

# from bpm_webapp.views.users import views
from web_app.views.users import views


urlpatterns = [   
    path('list/',views.ListAuthUserView.as_view(),name='authuser_list'),
    path('authuser_list/',views.CreateAuthUser.as_view(),name='authuser'),
    # path("json/list/", views.ListAuthUserInJsonFormat.as_view(), name="list_authuser_json"),
    # path("specific/", views.GetSpecificAuthUserView.as_view(), name="get_specific_user"),
    path("delete/", views.DeleteAuthUserView.as_view(), name="delete_specific_user"),
    # path("update/", views.UpdateAuthUserView.as_view(), name="update_specific_user"),
    path("checkauthusername/", views.CheckAuthUserNameView.as_view(), name="check_authuser_name"),
    path("checkemailaddress/", views.CheckEmailAddress.as_view(), name="check_emailaddress"),
    # path("check/employee/id", views.CheckEmployeeId.as_view(), name="check_employeeid"),
    path("checkupdateemailaddress/", views.CheckUpdatEmailView.as_view(), name="check_update_emailaddress"),
    path('activate/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='activate_and_reset_password'),
    # path("generate/new/activation/link/", views.GenerateUserActivationLinkAgainJsonView.as_view(), name="generate_new_activiation_link"),
    path("get/designation/of/departs",views.GetDesignationOfDepartment.as_view(),name='get_designation_of_departments'),
]