from django.contrib import admin
from .models import DepartmentHead,QualityDepartment,Reporter

# Register your models here.
admin.site.register(DepartmentHead)
admin.site.register(QualityDepartment)
admin.site.register(Reporter)