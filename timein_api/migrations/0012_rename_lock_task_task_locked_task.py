# Generated by Django 4.0.5 on 2022-07-18 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timein_api', '0011_alter_task_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='lock_task',
            new_name='locked_task',
        ),
    ]