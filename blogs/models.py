from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post', kwargs={'post_id': self.pk})

    def get_update_url(self):
        return reverse('blogs:edit_post', kwargs={'post_id': self.pk})

    def get_delete_url(self):
        return reverse('blogs:delete_post', kwargs={'post_id': self.pk})
