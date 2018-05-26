from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

from .forms import CustomUserCreationForm


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registeration form.
        form = CustomUserCreationForm()
        return render(request, 'bloggers/register.html', {'form': form})

    else:
        # Process completed form.
        bound_form = CustomUserCreationForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            # Log the user in then redirect to the home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))

        return render(request, 'bloggers/register.html', {'form': bound_form})
