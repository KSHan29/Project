from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.utils.async_logging import async_log

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_url = models.URLField()
    html_url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    show = models.BooleanField(default=True)
    languages = models.JSONField(default=dict)
    languages_lines = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_synced = models.BooleanField(default=False)
    profile_img_url = models.URLField()
    def __str__(self):
        return self.user.username

class ResumeSummary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='uploads/pdfs/')
    images = models.ImageField(upload_to='uploads/images/resumes/', null=True)
    personal = models.JSONField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    education = models.JSONField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    experience = models.JSONField(blank=True, null=True)
    projects = models.JSONField(blank=True, null=True)
    def __str__(self):
        return self.user.username

# Automatically create or update UserProfile whenever a User is created or updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        async_log('Created user profile')
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    async_log('Saved user profile')
