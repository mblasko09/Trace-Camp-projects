from rest_framework import serializers
from kick_api import models

class kick_starter_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.kick_starter_model
        fields = ('id', 'backers_count', 'blurb', 'category')
