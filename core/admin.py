from django.contrib import admin
from .models import Student, UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone_number', 'created_at']
    list_filter = ['role', 'created_at']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'phone_number']
    readonly_fields = ['created_at']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'current_class', 'email', 'enrollment_date', 'is_active']
    list_filter = ['current_class', 'gender', 'is_active', 'enrollment_date']
    search_fields = ['first_name', 'last_name', 'email', 'parent_name']
    readonly_fields = ['enrollment_date', 'created_by', 'updated_at']
    list_per_page = 50
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender')
        }),
        ('Academic Information', {
            'fields': ('current_class', 'enrollment_date')
        }),
        ('Contact Information', {
            'fields': ('address', 'parent_name', 'parent_phone')
        }),
        ('Status', {
            'fields': ('is_active', 'created_by', 'updated_at')
        }),
    )
