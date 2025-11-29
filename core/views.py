from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Student, UserProfile
from .forms import StudentForm

# Static pages
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

# Authentication views
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'core/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def dashboard(request):
    """Dashboard showing statistics and quick actions"""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        messages.error(request, 'User profile not found. Please contact administrator.')
        return redirect('home')
    
    total_students = Student.objects.filter(is_active=True).count()
    recent_students = Student.objects.filter(is_active=True).order_by('-enrollment_date')[:5]
    
    context = {
        'profile': profile,
        'total_students': total_students,
        'recent_students': recent_students,
    }
    return render(request, 'core/dashboard.html', context)

# Student management views (protected)
@login_required
def student_list(request):
    """List all students with search functionality"""
    query = request.GET.get('q', '')
    students = Student.objects.filter(is_active=True)
    
    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(current_class__icontains=query)
        )
    
    context = {
        'students': students,
        'query': query,
    }
    return render(request, 'core/student_list.html', context)

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk, is_active=True)
    return render(request, 'core/student_detail.html', {'student': student})

@login_required
def student_create(request):
    """Create new student - requires authentication"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.save()
            messages.success(request, f'Student {student.first_name} {student.last_name} added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form, 'title': 'Add Student'})

@login_required
def student_update(request, pk):
    """Update student - requires authentication"""
    student = get_object_or_404(Student, pk=pk, is_active=True)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student.first_name} {student.last_name} updated successfully!')
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form, 'title': 'Edit Student', 'student': student})

@login_required
def student_delete(request, pk):
    """Soft delete student - requires authentication"""
    student = get_object_or_404(Student, pk=pk, is_active=True)
    
    if request.method == 'POST':
        student.is_active = False
        student.save()
        messages.success(request, f'Student {student.first_name} {student.last_name} removed successfully!')
        return redirect('student_list')
    
    return render(request, 'core/student_confirm_delete.html', {'student': student})

# REST API ViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(is_active=True)
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
