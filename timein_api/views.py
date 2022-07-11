from rest_framework import viewsets, permissions

from .auth_util import get_user
from .models import Project, Task, Category, Period, Comment
from .serializers import ProjectSerializer, ProjectTaskSerializer, CategorySerializer, PeriodSerializer, \
    CommentSerializer, \
    SubtaskSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Project.objects.filter(user=get_user(self.request))

    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(user=get_user(self.request),
                        title=self.request.data['title'],
                        color=self.request.data['color'],
                        icon=self.request.data['icon'])

    permission_classes = (permissions.IsAuthenticated,)


class ProjectTaskViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Task.objects.filter(project=self.kwargs['project_pk'])

    serializer_class = ProjectTaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

class OngoingTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(parent_task=None, time_spent__gt=0)
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SubtaskViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Task.objects.filter(parent_task=self.kwargs['task_pk'])

    serializer_class = SubtaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Category.objects.filter(user=get_user(self.request))

    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=get_user(self.request),
                        title=self.request.data['title'],
                        color=self.request.data['color'])

    permission_classes = (permissions.IsAuthenticated,)


class PeriodViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Period.objects.filter(task=self.kwargs['task_pk'])

    serializer_class = PeriodSerializer

    permission_classes = (permissions.IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Comment.objects.filter(task=self.kwargs['task_pk'])

    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)