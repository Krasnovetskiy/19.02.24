from django.contrib import admin
from .models import Category, Good, Tag


class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'active', 'category', 'create', 'update']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['price', 'active']


class GoodAdminInline(admin.StackedInline):
    model = Good.tags.through
    extra = 2
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']
    inlines = [GoodAdminInline]


admin.site.register(Category)
admin.site.register(Good, GoodAdmin)
admin.site.register(Tag, TagAdmin)
