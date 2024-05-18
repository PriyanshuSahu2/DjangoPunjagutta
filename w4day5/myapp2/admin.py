from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['student', 'phone', 'city']


admin.site.register(Student, StudentAdmin)
admin.site.register(Contact, ContactAdmin)
