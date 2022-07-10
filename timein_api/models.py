from django.db import models


class Project(models.Model):
    user = models.EmailField(max_length=255, null=True)
    title = models.CharField(max_length=50)
    color = models.IntegerField()
    icon = models.ImageField(upload_to='project_icons/')


class Category(models.Model):
    user = models.EmailField(max_length=255, null=True)
    title = models.CharField(max_length=50)
    color = models.IntegerField()

class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True,
        blank=True
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

class Period(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    period = models.OneToOneField(
        Period,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    content = models.TextField()