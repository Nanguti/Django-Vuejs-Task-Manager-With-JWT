from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task, Category, TaskUserAssignment
from .serializers import TaskSerializer, CategorySerializer
from .permissions import IsSuperUserOrAssignedUser
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.response import Response


class LatestPagination(PageNumberPagination):
    page_size = 10

class TaskListCreateAPIView(generics.ListCreateAPIView):
    paginator = LatestPagination()
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
    paginator = LatestPagination()
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CustomUserViewSet(DjoserUserViewSet):
    pagination_class = LatestPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsSuperUserOrAssignedUser]