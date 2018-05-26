"""Defines URL patterns for bloggers."""

from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'bloggers'
urlpatterns = [
    # Login page
    path('login/', login, {'template_name' : 'bloggers/login.html'}, name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Register
    path('register/', views.register, name='register'),
]
