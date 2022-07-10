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
    def create(self, validated_data):
        validated_data["task"] = Task.objects.get(parent_task=self.context["view"].kwargs["task_pk"])
        print(validated_data)
        return Period.objects.create(**validated_data)

    class Meta:
        model = Period
        fields = ('start_time', 'end_time')


class CommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["task"] = Task.objects.get(parent_task=self.context["view"].kwargs["task_pk"])
        print(validated_data)
        return Comment.objects.create(**validated_data)

    class Meta:
        model = Comment
        fields = ('period', 'content')


class TaskSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["project"] = Project.objects.get(pk=self.context["view"].kwargs["project_pk"])
        print(validated_data)
        return Task.objects.create(**validated_data)

    class Meta:
        model = Task
        fields = ('category', 'parent_task', 'lock_task', 'title', 'desc', 'time_spent', 'is_done')


class SubtaskSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["parent_task"] = Task.objects.get(parent_task=self.context["view"].kwargs["task_pk"])
        print(validated_data)
        return Task.objects.create(**validated_data)

    class Meta:
        model = Task
        fields = ('category', 'lock_task', 'title', 'desc', 'time_spent', 'is_done')