from rest_framework import serializers

from .models import Project, Task, Category, Range, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'color', 'icon')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'color')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('project', 'category', 'parent_task', 'lock_task', 'title', 'desc', 'time_spent', 'is_done')

class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = ('start_time', 'end_time')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('range', 'content')
