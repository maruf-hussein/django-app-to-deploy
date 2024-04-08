from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("fullname", "image", "uniqueId")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "fullname", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "fullname", "uniqueId", "is_staff")
    search_fields = ("email", "fullname", "uniqueId")
    ordering = ("email",)
    filter_horizontal = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ("uniqueId",)
        return self.readonly_fields


admin.site.register(User, UserAdmin)
