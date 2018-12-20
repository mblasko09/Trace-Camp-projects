from django.shortcuts import render
from rest_framework import viewsets
from kick_api import models
from kick_api import serializers
# Create your views here.
class get_kick(viewsets.ModelViewSet):
    queryset = models.kick_starter_model.objects.all()
    serializer_class = serializers.kick_starter_serializer
