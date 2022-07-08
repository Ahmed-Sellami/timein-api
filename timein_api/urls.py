from django.urls import path, include
from rest_framework_nested import routers

from .views import ProjectViewSet, TaskViewSet, CategoryViewSet, PeriodViewSet, CommentViewSet, UserProfileViewSet, \
   SimpleTaskViewSet, SimpleCommentViewSet, TaskSubtasksViewSet

router = routers.DefaultRouter()
router.register(r'tasks', SimpleTaskViewSet, basename='tasks')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'periods', PeriodViewSet, basename='periods')
router.register(r'users', UserProfileViewSet)
router.register(r'comments', SimpleCommentViewSet, basename='comments')

projects_tasks_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_tasks_router.register(r'tasks', TaskViewSet, basename='project-tasks')

tasks_other_router = routers.NestedSimpleRouter(projects_tasks_router, r'tasks', lookup='task')
tasks_other_router.register(r'comments', CommentViewSet, basename='project-comments')
tasks_other_router.register(r'periods', PeriodViewSet, basename='project-periods')
tasks_other_router.register(r'subtasks', TaskSubtasksViewSet, basename='project-subtasks')

urlpatterns = [
   path('', include(router.urls)),
   path('', include(projects_tasks_router.urls)),
   path('', include(tasks_other_router.urls))
]