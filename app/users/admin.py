# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    model = User
    readonly_fields = ("date_joined", "last_login")
    list_filter = ("is_superuser", "is_staff", "is_active", "date_joined")
    ordering = ("username",)
