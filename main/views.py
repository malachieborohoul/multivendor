from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics, permissions
# Create your views here.

class VendorList(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    permission_classes = [permissions.IsAuthenticated]