from django.contrib import admin

from myapp.models import Author, Book, Publisher

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'profile_pic']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publishers']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address'] 


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
