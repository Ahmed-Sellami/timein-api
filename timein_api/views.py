from django.shortcuts import render
from rest_framework import viewsets

from .models import Project, Task, Category, Range, Comment
from .serializers import ProjectSerializer, TaskSerializer, CategorySerializer, RangeSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RangeViewSet(viewsets.ModelViewSet):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
