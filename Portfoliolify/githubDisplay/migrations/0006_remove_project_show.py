# Generated by Django 4.2.13 on 2024-07-03 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('githubDisplay', '0005_userprofile_selected_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='show',
        ),
    ]