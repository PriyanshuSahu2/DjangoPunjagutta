from django.contrib import admin

# Register your models here.
from django.contrib.admin.decorators import register

from myapp.models import Student


@register(Student)
class StudntAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address']
