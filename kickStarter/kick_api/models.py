from django.db import models

# Create your models here.
class kick_starter_model(models.Model):
    backers_count = models.IntegerField()
    blurb = models.TextField()
    category = models.TextField()
    class Meta:
        ordering = ['backers_count']
