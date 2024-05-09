from rest_framework import serializers
from base.models import Vendor,PurchaseOrder,VendorPerformance



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    purchase_order = PurchaseOrderSerializer(many=True, read_only = True)
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPerformance
        fields = '__all__'