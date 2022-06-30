from django.urls import path, include
from rest_framework import routers

from .views import ProjectViewSet, TaskViewSet, CategoryViewSet, RangeViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'ranges', RangeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
   path('', include(router.urls)),
]