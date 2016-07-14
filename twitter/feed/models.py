from __future__ import unicode_literals
from django.db import models

import datetime

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=200)
  username = models.CharField(max_length=200)

  def __str__(self):
    return str(self.username)

class Tweet(models.Model):
  text = models.CharField(blank=True, max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  timestamp = models.DateTimeField('date published', default=datetime.datetime.now)
  reply = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
  retweet = models.ForeignKey('self', related_name='retweets', null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return "%s: %s" % (self.user, self.text)

