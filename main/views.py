from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics, permissions, pagination, viewsets
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
    serializer_class = serializers.ProductSerializer
    # pagination_class= pagination.LimitOffsetPagination 

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


class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = models.CustomerAddress.objects.all()
    serializer_class= serializers.CustomerAddressSerializer

    # def get_queryset(self):
    #     customer_id = self.kwargs['pk']
    #     customer = models.Customer.objects.get(id=customer_id)
    #     customer_addresses = models.CustomerAddress.objects.filter(customer=customer)
    #     return customer_addresses

class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = models.ProductRating.objects.all()
    serializer_class= serializers.ProductRatingSerializer



class CategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class= pagination.LimitOffsetPagination 

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategorySerializer