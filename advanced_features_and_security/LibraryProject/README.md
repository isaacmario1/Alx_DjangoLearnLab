# LibraryProject

This is a basic Django project created as part of the ALX Django learning lab.

## Getting Started
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate` (Windows)
3. Install Django: `pip install django`
4. Run the server: `python manage.py runserver`


# Permissions & Groups Setup

This app uses Django’s built-in permissions system:

Groups:
- Editors → can_create, can_edit
- Viewers → can_view
- Admins → all permissions

Views use `@permission_required` decorators to restrict access.

## Author
Isaac Mwangale