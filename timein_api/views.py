import simplejson
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from .auth_util import get_user
from .models import Project, Task, Category, Period, Comment
from .serializers import ProjectSerializer, TaskSerializer, CategorySerializer, PeriodSerializer, CommentSerializer, \
    SubtaskSerializer
from .task_util import get_all_tasks, get_all_tasks_dict


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

class AllView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.filter(user=get_user(self.request))
        projects = Project.objects.filter(user=get_user(self.request))
        projects_detail = []
        for p in projects:
            tasks_node = get_all_tasks(p.id, None)
            tasks = []
            for c in tasks_node.children:
                tasks.append(get_all_tasks_dict(c))
            projects_detail.append(
                {'title': p.title, 'color': p.color, 'icon': p.icon.url if p.icon else '', 'tasks': tasks}
            )

        json = simplejson.dumps(
            {'projects': projects_detail,
             'categories': [{'id': c.id, 'title': c.title, 'color': c.color} for c in categories]}
        )
        return HttpResponse(json, content_type='application/json')

    permission_classes = (permissions.IsAuthenticated,)
