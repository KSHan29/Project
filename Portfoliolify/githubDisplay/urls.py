from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/projects/', views.projects_data_view, name='get_projects'),
    path('api/profile/', views.profile_data_view, name='get_profile'),
    path('sync/', views.sync_projects_view, name='sync_projects'),
    path('projects/', views.user_projects_view, name='user_projects'),
]
