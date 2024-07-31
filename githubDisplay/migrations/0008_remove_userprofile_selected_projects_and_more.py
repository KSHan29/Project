# Generated by Django 4.2.13 on 2024-07-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('githubDisplay', '0007_project_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='selected_projects',
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.JSONField(default=dict),
        ),
    ]