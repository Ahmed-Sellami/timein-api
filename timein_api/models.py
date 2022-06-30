from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    color = models.IntegerField()
    icon = models.BinaryField(max_length=1024 * 1024 * 5)  # 5 MB icon

class Category(models.Model):
    title = models.CharField(max_length=50)
    color = models.IntegerField()

class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    parent_task = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subtasks',
        null=True,
        blank=True
    )
    lock_task = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='prerequisites',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500, null=True, blank=True)
    time_spent = models.IntegerField(default=0)  # in seconds
    is_done = models.BooleanField()

class Range(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Comment(models.Model):
    range = models.OneToOneField(
        Range,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    content = models.TextField()