# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task, Category, TaskUserAssignment
from .serializers import TaskSerializer, CategorySerializer
from .permissions import IsOwnerOrAdmin, IsSuperUserOrAssignedUser
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class LatestTaskPagination(PageNumberPagination):
    page_size = 3

class TaskListCreateAPIView(generics.ListCreateAPIView):
    paginator = LatestTaskPagination()
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        
        assignee_id = self.request.data.get('assignee')
        if assignee_id:
            assignee = get_object_or_404(User, pk=assignee_id)
            TaskUserAssignment.objects.create(user=assignee, task=instance)


class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsSuperUserOrAssignedUser]


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
