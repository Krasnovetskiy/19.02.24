from django.contrib import admin
from .models import UserStat

class UserStatAdmin(admin.ModelAdmin):
    list_display =  ['id', 'created_at']

admin.site.register(UserStat, UserStatAdmin)