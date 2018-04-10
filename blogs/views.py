from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import BlogPost
from .forms import PostForm, ContentForm

# Create your views here.

def index(request):
    """Show the home page"""
    return render(request, 'blogs/index.html')


@login_required
def posts(request):
    """Show all posts."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts' : posts}
    return render(request, 'blogs/posts.html', context)


@login_required
def post(request, post_id):
    """Show the post's contents"""
    post = get_object_or_404(BlogPost, id=post_id)
    context = {'post' : post}
    return render(request, 'blogs/post.html', context)


@login_required
def add_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted; creater a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    
    context = {'form' : form}
    return render(request, 'blogs/add_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit existing post"""
    post = get_object_or_404(BlogPost, id=post_id)
    check_post_owner(request.user, post.owner)
    if request.method != 'POST':
        # Initial request; pre-fill form with existing data.
        form = ContentForm(instance=post)
    else:
        # POST data submitted; process data
        form = ContentForm(instance=post, data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.id = post_id
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))
    
    context = {'post' : post, 'form' : form}
    return render(request, 'blogs/edit_post.html', context)


def check_post_owner(curr_user, owner):
    if curr_user != owner:
        raise Http404
