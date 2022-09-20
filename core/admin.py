from django.contrib import admin
from core import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary']
    search_fields = ['name']

# Register your models here.
