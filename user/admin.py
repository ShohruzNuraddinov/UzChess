from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser

    list_display = [
        'full_name',
        "phone_number",
        'email',
        'birth_date',
        'is_admin',
        'auth_type',
        'is_active',

    ]
    list_filter = []
    fieldsets = [
        (None, {"fields": [
            "phone_number",
            'email',
            'full_name',
            'birth_date',
            'auth_type',
            'image',
            'is_admin',
            'password',
        ]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "phone_number",
                    'email',
                    'full_name',
                    'birth_date',
                    'auth_type',
                    'image',
                    'is_admin',
                    'password1',
                    'password2',
                ],
            },
        ),
    ]
    ordering = ["id"]
    filter_horizontal = []
    search_fields = [
        "phone_number",
        'full_name',
        'email'
    ]


admin.site.register(CustomUser, CustomUserAdmin)
