from django.urls import   path
from .views import UserListCreate, TodoListCreate, TodoDetailUpdateDelete

urlpatterns = [
    path('users/', UserListCreate.as_view(), name=  'user-list-create'),
    path('todos/', TodoListCreate.as_view(), name=  'todo-list-create'),
    path('todos/<int:pk>/', TodoDetailUpdateDelete.as_view(), name=  'todo-detail-update-delete'),
]
