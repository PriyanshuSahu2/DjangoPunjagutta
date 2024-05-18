from django.contrib import admin

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'age']


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
