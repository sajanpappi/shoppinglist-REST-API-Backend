from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class Meta:
        model = Item
        fields = ['id', 'name', 'quantity', 'price']

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'quantity', 'price']
