from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'gender', 'teacher']
  

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
