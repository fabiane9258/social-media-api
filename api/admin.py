from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "role", "is_active", "is_staff")
    search_fields = ("username", "email")
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("role", "bio", "profile_picture_url")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "bio", "profile_picture_url")}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at")
    search_fields = ("author__username", "content")
    list_filter = ("created_at",)
