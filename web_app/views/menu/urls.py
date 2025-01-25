from django.urls import path

from web_app.views.menu import views

urlpatterns = [   
    path('list/',views.ListMenuView.as_view(),name='menu_list'),
    path('menu_list/',views.CreateMenu.as_view(),name='menu'),
    path("json/list/", views.ListMenuInJsonFormat.as_view(), name="list_menu_json"),
    path("specific/", views.GetSpecificMenuView.as_view(), name="get_specific_menu"),
    path("update/", views.UpdateMenuView.as_view(), name="update_specific_menu"),
    path("delete/", views.DeleteMenuView.as_view(), name="delete_specific_menu"),
    path("menu/name/", views.CheckMenusNameView.as_view(), name="check_menu_name"),
    path("update/menu/name/", views.CheckUpdateMenusNameView.as_view(), name="check_update_menu_name"),
    path("get/child/menus", views.GetChildMenus.as_view(), name="get_child_menus"),
]