# Generated by Django 4.2.13 on 2024-07-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('githubDisplay', '0011_resumesummary_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumesummary',
            name='education',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resumesummary',
            name='experience',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resumesummary',
            name='personal',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resumesummary',
            name='projects',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resumesummary',
            name='skills',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resumesummary',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
