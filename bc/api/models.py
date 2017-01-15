from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class BucketList(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)


class BucketListItem(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=255, blank=True)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    bucketlist = models.ForeignKey(BucketList)

