# Generated by Django 4.0.5 on 2022-07-06 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timein_api', '0003_remove_project_username_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timein_api.task'),
        ),
    ]
