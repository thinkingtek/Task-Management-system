from django.contrib import admin
from .models import User, Profile
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (str, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'username', 'is_active', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('email', 'username')


admin.site.register(Profile)
