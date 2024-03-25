# urls.py
from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/detail/', TaskDetailAPIView.as_view(), name='task-detail-detail'), # 
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
]
