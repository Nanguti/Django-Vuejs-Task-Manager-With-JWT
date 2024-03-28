from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView,CustomUserViewSet, TaskDetailAPIView, CategoryRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/detail/', TaskDetailAPIView.as_view(), name='task-detail-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='destroy-category'),
]
