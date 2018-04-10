"""Defines URL patterns for blogs"""

from django.urls import path, re_path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page that shows the posts
    re_path(r'^posts/$', views.posts, name='posts'),
    # Showing each post on it's own
    re_path(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),
    # Adding a new post
    re_path(r'^add_post/$', views.add_post, name='add_post'),
    # Editing an existing post
    re_path(r'edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    
]
