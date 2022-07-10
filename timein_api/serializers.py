from rest_framework import serializers

from .models import Project, Task, Category, Period, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('user', 'title', 'color', 'icon')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('user', 'title', 'color')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('task', 'start_time', 'end_time')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('task', 'period', 'content')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('project', 'category', 'parent_task', 'lock_task', 'title', 'desc', 'time_spent', 'is_done')
