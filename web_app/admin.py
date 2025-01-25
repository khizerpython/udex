from django.contrib import admin

# Register your models here.
from django.contrib import admin
from web_app.models import Department,AuthUser,Role,Designation,City,Menus,Country
# Register your models here.
admin.site.register(Department)
admin.site.register(AuthUser)
admin.site.register(Role)
admin.site.register(Designation)
admin.site.register(City)
admin.site.register(Menus)
admin.site.register(Country)
