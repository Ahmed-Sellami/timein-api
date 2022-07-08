from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.models import User
from .models import Project, Task, Category, Period, Comment
from .serializers import ProjectSerializer, TaskSerializer, CategorySerializer, PeriodSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Project.objects.filter(user=get_user(self.request))

    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(user=get_user(self.request),
                        title=self.request.data['title'],
                        color=self.request.data['color'],
                        icon=self.request.data['icon'])

    # permission_classes = (permissions.IsAuthenticated,)


class TaskViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Task.objects.filter(project=self.kwargs['project_pk'])

    serializer_class = TaskSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class TaskSubtasksViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Task.objects.filter(parent_task=self.kwargs['task_pk'])

    serializer_class = TaskSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class SimpleTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Category.objects.filter(user=get_user(self.request))

    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=get_user(self.request),
                        title=self.request.data['title'],
                        color=self.request.data['color'])

    # permission_classes = (permissions.IsAuthenticated,)


class PeriodViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Period.objects.filter(task=self.kwargs['task_pk'])

    serializer_class = PeriodSerializer

    # permission_classes = (permissions.IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Comment.objects.filter(task=self.kwargs['task_pk'])

    serializer_class = CommentSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class SimpleCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_authenticators(self):
        return super().get_authenticators()


def get_user(request):
    jwt_object = JWTAuthentication()
    header = jwt_object.get_header(request)
    raw_token = jwt_object.get_raw_token(header)
    validated_token = jwt_object.get_validated_token(raw_token)
    user = jwt_object.get_user(validated_token)
    print('User: ' + str(user))
    authorized_users = User.objects.filter(email=user)
    if not authorized_users:
        return None
    return user
