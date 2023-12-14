from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics, permissions, pagination
# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer,
    pagination_class= pagination.LimitOffsetPagination 

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class OrderDetail(generics.ListAPIView):
    # queryset = models.Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer
    def get_queryset(self):
        orderId = self.kwargs['pk']

        order = models.Order.objects.get(id=orderId)
        order_items = models.OrderItem.objects.filter(order=order)

        return order_items

class OrderItemList(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer