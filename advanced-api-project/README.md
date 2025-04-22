# Advanced API Project: Book API with Generic Views

This API allows CRUD operations on Book objects using Django REST Framework’s generic views.

## Endpoints

| Endpoint | Method | Description | Permission |
|----------|--------|-------------|------------|
| `/api/books/` | GET | List all books | Public |
| `/api/books/<id>/` | GET | Retrieve book by ID | Public |
| `/api/books/create/` | POST | Create new book | Authenticated users |
| `/api/books/<id>/update/` | PUT/PATCH | Update book | Authenticated users |
| `/api/books/<id>/delete/` | DELETE | Delete book | Authenticated users |

## Permissions
- Read operations are open to all.
- Create/Update/Delete operations require the user to be logged in.

## Files Modified

- `api/views.py`: Contains all generic view classes
- `api/urls.py`: URL patterns for each view
- `advanced_api_project/urls.py`: Root project URL includes `/api/`
