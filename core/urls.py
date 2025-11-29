from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/students', views.StudentViewSet)

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    
    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Student management (protected)
    path('students/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/new/', views.student_create, name='student_create'),
    path('student/<int:pk>/edit/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    
    # API
    path('', include(router.urls)),
]
