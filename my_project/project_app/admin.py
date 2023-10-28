from django.contrib import admin

from .models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'family', 'background', 'photo_family', 'photo_person')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'background')
    prepopulated_fields = {"slug": ("first_name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
