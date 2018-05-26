from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import View

from .forms import ContentForm, PostForm
from .models import BlogPost


def index(request):
    """Show the home page"""
    posts = BlogPost.objects.all()
    context = {'posts' : posts[:3]}
    return render(request, 'blogs/index.html', context)


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
    owner = post.owner
    context = {'post' : post}
    return render(request, 'blogs/post.html', context)


@login_required
def add_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted; creater a blank form.
        form = PostForm()
        return render(request, 'blogs/add_post.html', {'form': form})

    else:
        # POST data submitted; process data.
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

        return render(request, 'blogs/add_post.html', {'form': bound_form})


@login_required
def edit_post(request, post_id):
    """Edit existing post"""
    if request.method != 'POST':
        # Initial request; pre-fill form with existing data.
        post = get_object_or_404(BlogPost, id=post_id)
        check_post_owner(request.user, post.owner)
        form = PostForm(instance=post)

    else:
        # POST data submitted; process data
        post = get_object_or_404(BlogPost, id=post_id)
        check_post_owner(request.user, post.owner)
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.id = post_id
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))

    return render(request, 'blogs/edit_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    """Deleting existing posts"""

    if request.method != 'POST':
        # Initial request; show the delete page
        post = get_object_or_404(BlogPost, id=post_id)
        check_post_owner(request.user, post.owner)
        return render(request, 'blogs/delete_post.html', {'post': post})

    else:
        # POST data submitted; process data
        post = get_object_or_404(BlogPost, id=post_id)
        check_post_owner(request.user, post.owner)
        post.delete()
        return HttpResponseRedirect(reverse('blogs:posts'))

def check_post_owner(curr_user, owner):
    if curr_user != owner:
        raise Http404
