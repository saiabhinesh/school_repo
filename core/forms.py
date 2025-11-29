from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'date_of_birth', 'gender', 'current_class', 'address',
            'parent_name', 'parent_phone'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'student@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 XXXXX XXXXX'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'current_class': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Full Address'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parent/Guardian Name'}),
            'parent_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 XXXXX XXXXX'}),
        }
        labels = {
            'first_name': 'First Name *',
            'last_name': 'Last Name *',
            'email': 'Email Address *',
            'phone_number': 'Phone Number',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'current_class': 'Class',
            'address': 'Address',
            'parent_name': 'Parent/Guardian Name',
            'parent_phone': 'Parent/Guardian Phone',
        }
