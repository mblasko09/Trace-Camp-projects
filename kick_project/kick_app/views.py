# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from kick_app.models import kick_campaign
from django.core import serializers

def get_kick(request, kick_id):
    kick_start = kick_campaign.objects.filter(id = kick_id)
    response = serializers.serialize("json", kick_start)
    return HttpResponse(response)
