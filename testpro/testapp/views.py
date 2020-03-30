from django.shortcuts import render
from rest_framework import viewsets
from.models import user_details
from.serializing import serialized_details
# Create your views here.
class user_register(viewsets.ModelViewSet):
    queryset=user_details.objects.all()
    serializer_class=serialized_details