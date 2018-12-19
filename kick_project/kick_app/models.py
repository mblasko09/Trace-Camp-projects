# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class kick_campaign(models.Model):
    backers_count = models.IntegerField()
    blurb = models.TextField()
    category = models.TextField()
