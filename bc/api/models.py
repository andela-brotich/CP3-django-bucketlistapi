from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class BucketList(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)


class BucketListItem(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=255, blank=True)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    bucketlist = models.ForeignKey(BucketList, null=True, blank=True)

