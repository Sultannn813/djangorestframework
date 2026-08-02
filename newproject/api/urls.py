
from django.urls import path
from .views import get_users, create_users  # <-- Импорт

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_users, name='create_user'),
    path('users/<int:pk>/', get_users, name='get_user'),
    path('users/<int:pk>/update/', get_users, name='update_user'),
    path('users/<int:pk>/delete/', get_users, name='delete_user')
]
