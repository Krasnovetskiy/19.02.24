from django.contrib import admin
from .models import Category, Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'active']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['price', 'active']

admin.site.register(Category)
admin.site.register(Good)
