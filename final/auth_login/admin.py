from django.contrib import admin
from auth_login.models import Guest, SuperAdmin
# Register your models here.

admin.site.register(Guest)
admin.site.register(SuperAdmin)