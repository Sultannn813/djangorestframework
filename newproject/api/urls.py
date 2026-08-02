
from django.urls import path
from .views import get_users, create_users  # <-- Импорт

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_users, name='create_user'),  # <-- Маршрут
]
