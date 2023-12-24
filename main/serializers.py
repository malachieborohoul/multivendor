from rest_framework import serializers
from rest_framework.fields import empty
from . import models
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields =['id','user', 'address']
        
    def __init__(self, *args, **kwargs):
        super(VendorSerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth=1

# 
class ProductSerializer(serializers.ModelSerializer):
    product_ratings= serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields =['id','category', 'vendor','title','detail','price', 'product_ratings']
        
    def __init__(self, *args, **kwargs):
        super(ProductSerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth=1


class CategorySerializer(serializers.ModelSerializer):
    product_ratings= serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.ProductCategory
        fields =['id','title','detail']
        
    def __init__(self, *args, **kwargs):
        super(CategorySerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth=
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields =['id','user', 'mobile']
        
    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields =['id','customer']
        
    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields =['id','order', 'product']
        
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields =['id','order', 'product']
        
    def __init__(self, *args, **kwargs):
        super(OrderItemSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields =['id','customer', 'address', 'default_address']
        
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields =['id','customer', 'product', 'rating', 'reviews','add_time']
        
    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 