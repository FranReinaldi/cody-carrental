from django.contrib import admin
from .models import CustomUser, UserType

admin.site.register(CustomUser)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['user', 'type']


admin.site.register(UserType, UserTypeAdmin)
