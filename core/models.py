from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """Extended user profile with role-based permissions"""
    ROLE_CHOICES = [
        ('principal', 'Principal'),
        ('teacher', 'Teacher'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.get_role_display()})"
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    CLASS_CHOICES = [
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    current_class = models.CharField(max_length=2, choices=CLASS_CHOICES, default='6')
    address = models.TextField(blank=True)
    parent_name = models.CharField(max_length=200, blank=True)
    parent_phone = models.CharField(max_length=15, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='students_created')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Class {self.current_class}"
    
    class Meta:
        ordering = ['current_class', 'first_name', 'last_name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
