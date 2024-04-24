from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Item
from .serializers import ItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]  # Allow access to anyone

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]  # Allow access to anyone

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]  # Allow access to anyone