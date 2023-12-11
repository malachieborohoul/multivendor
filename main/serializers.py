from rest_framework import serializers
from rest_framework.fields import empty
from . import models
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields =['user', 'address']
        
    def __init__(self, *args, **kwargs):
        super(VendorSerializer,self).__init__(*args, **kwargs)
        self.Meta.depth=1