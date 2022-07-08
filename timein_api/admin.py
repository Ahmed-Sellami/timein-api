from django.contrib import admin

# Register your models here.
from .models import Project, Task, Category, Period, Comment

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Period)
admin.site.register(Comment)