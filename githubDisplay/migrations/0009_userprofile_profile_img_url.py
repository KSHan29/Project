# Generated by Django 4.2.13 on 2024-07-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('githubDisplay', '0008_remove_userprofile_selected_projects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_img_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]