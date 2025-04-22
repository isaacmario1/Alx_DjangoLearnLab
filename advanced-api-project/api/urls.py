# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet,
    BookViewSet,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    home
)

# ViewSet router setup (for DRF router-based URLs)
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

# URL patterns
urlpatterns = [
    # Home endpoint
    path('', home, name='home'),

    # Include ViewSet-based routes
    path('api/', include(router.urls)),

    # Book generic class-based views
    path('api/books/', BookListView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/create/', BookCreateView.as_view(), name='book-create'),
    path('api/books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('api/books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
