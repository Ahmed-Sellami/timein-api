# Generated by Django 4.0.5 on 2022-07-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timein_api', '0002_rename_range_period_project_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='username',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.EmailField(default='ahmedsellami526@gmail.com', max_length=255),
        ),
    ]