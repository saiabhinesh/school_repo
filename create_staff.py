# Create Staff Users Script
# Run this in Django shell: python manage.py shell < create_staff.py

from django.contrib.auth.models import User
from core.models import UserProfile

# Create Principal
print("Creating Principal account...")
principal_user, created = User.objects.get_or_create(
    username='principal',
    defaults={
        'first_name': 'Principal',
        'last_name': 'Admin',
        'email': 'principal@srimajety.edu.in',
        'is_staff': True,
    }
)
if created:
    principal_user.set_password('principal123')  # Change this password!
    principal_user.save()
    UserProfile.objects.create(
        user=principal_user,
        role='principal',
        phone_number='+91 9700 622222'
    )
    print(f"✓ Principal account created: username='principal', password='principal123'")
else:
    print(f"✓ Principal account already exists")

# Create Teacher 1
print("\nCreating Teacher account...")
teacher_user, created = User.objects.get_or_create(
    username='teacher',
    defaults={
        'first_name': 'Teacher',
        'last_name': 'Staff',
        'email': 'teacher@srimajety.edu.in',
        'is_staff': True,
    }
)
if created:
    teacher_user.set_password('teacher123')  # Change this password!
    teacher_user.save()
    UserProfile.objects.create(
        user=teacher_user,
        role='teacher',
        phone_number='+91 8019 734989'
    )
    print(f"✓ Teacher account created: username='teacher', password='teacher123'")
else:
    print(f"✓ Teacher account already exists")

print("\n" + "="*60)
print("STAFF ACCOUNTS CREATED SUCCESSFULLY!")
print("="*60)
print("\nLogin Credentials:")
print("-" * 60)
print("Principal:")
print("  Username: principal")
print("  Password: principal123")
print("  URL: http://127.0.0.1:8000/login/")
print()
print("Teacher:")
print("  Username: teacher")
print("  Password: teacher123")
print("  URL: http://127.0.0.1:8000/login/")
print("-" * 60)
print("\n⚠️  IMPORTANT: Change these passwords after first login!")
print("="*60)
