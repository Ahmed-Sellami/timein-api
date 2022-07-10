from django.urls import path, include
from rest_framework_nested import routers

from .views import ProjectViewSet, ProjectTaskViewSet, CategoryViewSet, PeriodViewSet, CommentViewSet, \
   SubtaskViewSet, AllView, TaskViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'tasks', TaskViewSet, basename='tasks')

projects_tasks_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_tasks_router.register(r'tasks', ProjectTaskViewSet, basename='project-tasks')

tasks_other_router = routers.NestedSimpleRouter(router, r'tasks', lookup='task')
tasks_other_router.register(r'comments', CommentViewSet, basename='project-comments')
tasks_other_router.register(r'periods', PeriodViewSet, basename='project-periods')
tasks_other_router.register(r'subtasks', SubtaskViewSet, basename='project-subtasks')

urlpatterns = [
   path('', include(router.urls)),
   path('', include(projects_tasks_router.urls)),
   path('', include(tasks_other_router.urls)),
   path('all/', AllView.as_view())
]