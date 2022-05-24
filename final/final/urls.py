from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from core.views import BookViewSet, JournalViewSet
from auth_login.views import admin_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('books/', BookViewSet.as_view({'get': 'get_books', 'post': 'add_book'})),
    path('books/<int:book_id>', BookViewSet.as_view({'get': 'get_book', 'put': 'update_book', 'delete': 'delete_book'})),
    path('journals/', JournalViewSet.as_view({'get': 'get_journals', 'post': 'add_journal'})),
    path('journals/<int:j_id>', JournalViewSet.as_view({'get': 'get_journal', 'put': 'update_journal', 'delete': 'delete_journal'})),
    path('login/', admin_user),
]

