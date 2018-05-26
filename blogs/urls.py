"""Defines URL patterns for blogs"""

from django.urls import path, re_path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page that shows the posts
    path('posts/', views.posts, name='posts'),
    # Showing each post on it's own
    path('posts/<int:post_id>/', views.post, name='post'),
    # Adding a new post
    path('add_post/', views.add_post, name='add_post'),
    # Editing an existing post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Deleting a post
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

]
