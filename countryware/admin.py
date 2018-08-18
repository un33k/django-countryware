from django.contrib import admin

from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    search_fields = ('code', 'name',)
    ordering = ['code', 'name']
