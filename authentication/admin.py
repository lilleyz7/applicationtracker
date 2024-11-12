from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm
from .models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     add_form = RegisterForm
#     model = CustomUser
#     list_display = [
#         "email",
#         "first_name",
#     ]


admin.site.register(CustomUser)