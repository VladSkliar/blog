from django.db import models
from django.contrib.auth.models import User, AbstractUser
from minisite.settings import common

from sorl.thumbnail import ImageField


class Info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField('Date of birth')
    bio = models.CharField(max_length=255)
    image = ImageField(upload_to='photos/', blank=True, null=True)
    user = models.ForeignKey(User, related_name='info', unique=True)
    jabber = models.CharField(max_length=50, blank=True, null=True)
    skype = models.CharField(max_length=50, blank=True, null=True)
    other_contacts = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class UserRequest(models.Model):
    path = models.CharField(max_length=255)
    time = models.DateTimeField('request_time')

    def __str__(self):
        return '%s' % self.path


class ActionInfo(models.Model):
    date = models.DateField('Action date')
    action_name = models.CharField(max_length=50)
    object_name = models.CharField(max_length=50)
    object_info = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s' % (self.action_name,
                             self.object_name,
                             self.object_info)


class UserInvite(models.Model):
    email = models.EmailField(max_length=50)
    user = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    is_accept = models.BooleanField(default=False)

    class Meta:
        unique_together = ('email', 'user')
