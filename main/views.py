from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics
# Create your views here.

class VendorList(generics.ListAPIView):
    serializer_class = serializers.SellerSerializer
    queryset = models.Vendor.objects.all()