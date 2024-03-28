# urls.py
from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView,CustomUserViewSet, TaskDetailAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/detail/', TaskDetailAPIView.as_view(), name='task-detail-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='destroy-category'),
    path('users/', CustomUserViewSet.as_view({'get': 'list'}), name='user-list'),

]
