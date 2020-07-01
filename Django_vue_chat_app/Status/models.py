from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from django.db import models
from django.conf import settings
# Create your models here.
from datetime import datetime
class Status(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Content = models.CharField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes_post')

    def __str__(self):
        return self.Content

    def save(self,*args, **kwargs,):  # new
        if not self.slug:
            random_s=generate_random_string()
            self.slug = slugify(self.Content)+'-'+random_s
        return super().save(*args, **kwargs)



class Comments(models.Model):
    post = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='posts_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='commentor')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')

    def __str__(self):
        return self.comment

class Messages(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="username", related_name='sender',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="username", on_delete=models.CASCADE,
                                 related_name='receiver',
                                 null=True, blank=True)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.text
