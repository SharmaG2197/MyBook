from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, AdminUser

class BaseAccountAdmin(UserAdmin):
    # Remove username from fieldsets and add_fieldsets
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),

        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)  # Changed from 'username' to 'email'
    filter_horizontal = ('groups', 'user_permissions',)

@admin.register(Account)
class AccountAdmin(BaseAccountAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)

@admin.register(AdminUser)
class AdminUserAdmin(BaseAccountAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=True)
    
    def has_add_permission(self, request):
        return False
    


    # admin.py
