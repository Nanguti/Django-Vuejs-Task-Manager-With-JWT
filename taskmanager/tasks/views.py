# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .permissions import IsOwnerOrAdmin, IsSuperUserOrAssignedUser


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Regular users can only see tasks assigned to them
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Assign task owner as the current user
        serializer.save(owner=self.request.user)

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
