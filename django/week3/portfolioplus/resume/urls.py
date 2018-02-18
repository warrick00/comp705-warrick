from django.urls import path, include

from . import views

urlpatterns = [
    path(r'resume', views.home, name='resume'),
    path(r'resumeplus', views.home, name='resumeplus'),
    ]
