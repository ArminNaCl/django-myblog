from django.contrib import admin

from .models import User
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation  import ugettext_lazy as _
# Register your models here.

class UserAdmin(BaseUserAdmin,):
    list_display=['full_name','email','is_staff']
    list_filter = ['full_name','email','is_staff']
    change_password_form =AdminPasswordChangeForm
    ordering = ('full_name',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (_('authentication data'), {
            "fields": (
                'email',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('full_name',)
        }),
        (_('Permissions'), {
            "fields": ('is_staff','is_superuser' )
        }),
        (_('Important dates'), {
            "fields": ('last_login',)
        }),
    )


admin.site.register(User,UserAdmin)