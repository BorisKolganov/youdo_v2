from django.contrib import admin

from models import *


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Employee)
admin.site.register(Comment)
admin.site.register(Service)
admin.site.register(ServiceType, ServiceTypeAdmin)

# Register your models here.
