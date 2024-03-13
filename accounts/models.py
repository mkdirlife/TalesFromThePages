from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='profile/images/%Y/%m/%d/', null=True, blank=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile')