# Sri Majety High School - Django Project

A comprehensive school management system for Sri Majety High School, Guntur, Andhra Pradesh.

## Features

### Public Website
- ✅ Beautiful South Asian-themed design
- ✅ Home page with school information
- ✅ Services/Programs page
- ✅ Contact page with school details
- ✅ School logo integration

### Staff Management System
- ✅ Secure login system for teachers and principals
- ✅ Role-based access control
- ✅ Dashboard with statistics
- ✅ Student management (Add, Edit, View, Delete)
- ✅ Search functionality
- ✅ Comprehensive student profiles

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saiabhinesh/school_repo.git
   cd school_proj
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create staff accounts** (Already done - see credentials below)
   ```bash
   Get-Content create_staff.py | venv\Scripts\python.exe manage.py shell
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Public Website: http://127.0.0.1:8000/
   - Staff Login: http://127.0.0.1:8000/login/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Default Login Credentials

### Principal Account
- **Username:** `principal`
- **Password:** `principal123`
- **Role:** Principal
- **Permissions:** Full access to all student data

### Teacher Account
- **Username:** `teacher`
- **Password:** `teacher123`
- **Role:** Teacher
- **Permissions:** Full access to all student data

⚠️ **IMPORTANT:** Change these passwords after first login!

## Student Management

### Adding Students
1. Login with principal or teacher credentials
2. Go to Dashboard
3. Click "Add New Student"
4. Fill in the student information:
   - Personal details (name, email, phone, DOB, gender)
   - Academic info (class)
   - Contact info (address, parent details)
5. Submit the form

### Managing Students
- **View All Students:** Dashboard → "View All Students"
- **Search Students:** Use the search box on student list page
- **Edit Student:** Click "Edit" button on student detail page
- **Delete Student:** Click "Delete" button (soft delete - can be restored)

## Project Structure

```
school_proj/
├── core/                          # Main app
│   ├── migrations/               # Database migrations
│   ├── static/core/              # Static files
│   │   └── images/              # School logo and images
│   ├── templates/core/           # HTML templates
│   │   ├── home.html            # Public home page
│   │   ├── services.html        # Services page
│   │   ├── contact.html         # Contact page
│   │   ├── login.html           # Staff login page
│   │   ├── dashboard.html       # Staff dashboard
│   │   ├── student_list.html    # Student list
│   │   ├── student_detail.html  # Student details
│   │   ├── student_form.html    # Add/Edit student
│   │   └── student_confirm_delete.html
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── forms.py                 # Forms
│   ├── urls.py                  # URL routing
│   └── admin.py                 # Admin configuration
├── school_management/            # Project settings
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py                  # WSGI configuration
├── manage.py                     # Django management script
├── create_staff.py              # Script to create staff accounts
└── requirements.txt             # Python dependencies
```

## Database Models

### UserProfile
- Extends Django User model
- Fields: role (principal/teacher), phone_number
- Links staff members to their roles

### Student
- Comprehensive student information
- Fields:
  - Personal: first_name, last_name, email, phone, DOB, gender
  - Academic: current_class (6-10)
  - Contact: address, parent_name, parent_phone
  - Status: is_active, enrollment_date
  - Tracking: created_by, updated_at

## Contact Information

**Sri Majety High School**
- Address: Nallacheruvu 1st Lane, Guntur, Andhra Pradesh, India
- Primary Phone: +91 9700 622222
- Secondary Phone: +91 8019 734989
- Email: info@srimajety.edu.in

## Technologies Used

- **Backend:** Django 5.2.8
- **Database:** SQLite3
- **Frontend:** HTML, CSS (Vanilla)
- **Authentication:** Django Auth System
- **API:** Django REST Framework

## Development

### Creating Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Making Database Changes
```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

## License

© 2025 Sri Majety High School. All rights reserved.

## Support

For support or questions, contact: msaiabhinesh@gmail.com
