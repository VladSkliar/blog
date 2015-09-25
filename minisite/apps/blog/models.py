import datetime

from django.db import models
from django.contrib.auth.models import User

from minisite.settings import common
from ckeditor.fields import RichTextField
from model_utils.fields import MonitorField


class Post(models.Model):
    author = models.ForeignKey(User, related_name='author')
    title = models.CharField(max_length=128)
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    publication_date = models.DateField()
    last_modified = MonitorField(monitor='text', blank=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)


class PostRating(models.Model):
    user = models.CharField(max_length=50, blank=True)
    post = models.PositiveSmallIntegerField()
    value = models.PositiveSmallIntegerField(default=0)
    ip_address = models.IPAddressField(blank=True)

    class Meta:
        unique_together = ('user', 'post')
