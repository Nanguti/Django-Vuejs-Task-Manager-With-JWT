from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task, Category, TaskUserAssignment
from .serializers import TaskSerializer, CategorySerializer, UserSerializer
from .permissions import IsSuperUserOrAssignedUser
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.response import Response

from rest_framework import status
from rest_framework.response import Response

class LatestPagination(PageNumberPagination):
    page_size = 10

class CustomUserViewSet(DjoserUserViewSet):
    pagination_class = LatestPagination
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
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

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUserOrAssignedUser]