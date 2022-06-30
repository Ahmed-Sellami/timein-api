from django.contrib import admin

# Register your models here.
from .models import Project, Task, Category, Range, Comment

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Range)
admin.site.register(Comment)