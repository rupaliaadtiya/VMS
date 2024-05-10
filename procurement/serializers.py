from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = ('id', 'name', 'contact_details', 'address','vendor_code', 'created_at', 'updated_at')

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'