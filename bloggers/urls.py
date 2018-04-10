"""Defines URL patterns for bloggers."""

from django.urls import re_path
from django.contrib.auth.views import login

from . import views

app_name = 'bloggers'
urlpatterns = [
    # Login page
    re_path(r'^login/$', login, {'template_name' : 'bloggers/login.html'}, name='login'),
    # Logout page
    re_path(r'^logout/$', views.logout_view, name='logout'),
    # Register
    re_path(r'^register/$', views.register, name='register'),
]