from rest_framework import serializers
from rest_framework.fields import empty
from . import models
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields =['user', 'address']
        
    def __init__(self, *args, **kwargs):
        super(VendorSerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth=1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields =['category', 'vendor','title','detail','price']
        
    def __init__(self, *args, **kwargs):
        super(ProductSerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth=1

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields =['id','user', 'mobile']
        
    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields =['id','customer', 'order_time']
        
    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields =['id','order', 'product']
        
    def __init__(self, *args, **kwargs):
        super(OrderItemSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1 