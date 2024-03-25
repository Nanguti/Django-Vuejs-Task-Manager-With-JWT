from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  

class TaskSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    def get_owner_name(self, obj):
        return obj.owner.username if obj.owner else None

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'owner', 'owner_name', 'category', 'category_name', 'completed'] 
