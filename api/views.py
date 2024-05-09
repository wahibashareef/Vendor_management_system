from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Vendor, PurchaseOrder, VendorPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from django.db.models import Avg, F
from datetime import timedelta

#Vendor Profile Management
@api_view(['GET'])
def getVendor(request):
    vendor = Vendor.objects.all()
    serializer = VendorSerializer(vendor, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addVendor(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def getSingleVendor(request, id):
    try:
        vendor = Vendor.objects.get(pk=id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    except Vendor.DoesNotExist:
        return Response(status=404)  # Not found.

@api_view(['PUT'])
def updateVendor(request, id):
    try:
        vendor = Vendor.objects.get(pk=id)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)   # Bad request.
    except Vendor.DoesNotExist:
        return Response(status=404)  # Not found.

@api_view(['DELETE'])
def deleteVendor(request, id):
    try:
        vendor = Vendor.objects.get(pk=id)
    except Vendor.DoesNotExist:
        return Response(status=404)
    
    vendor.delete()
    return Response(status=404)

#Purchase Order Tracking
@api_view(['GET'])
def getOrders(request):
    purchase_order = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_order, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def purchaseOrder(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def getSingleOrder(request, id):
    try:
        order = PurchaseOrder.objects.get(pk=id)
        serializer = PurchaseOrderSerializer(order, data=request.data)
        return Response(serializer.data)
    except PurchaseOrder.DoesNotExist:
        return Response(status=404)
    
@api_view(['PUT'])
def updateOrder(request, id):
    try:
        order = PurchaseOrder.objects.get(pk=id)
        serializer = PurchaseOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    except PurchaseOrder.DoesNotExist:
        return Response(status=404)

@api_view(['DELETE'])
def deleteOrder(request, id):
    try:
        order = PurchaseOrder.objects.get(pk=id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=404)
    order.delete()
    return Response(status=404)

#vendor performance evaluation
@api_view(['GET'])
def get_vendor_performance(request, id):
    try:
        vendor = Vendor.objects.get(pk=id)
    except Vendor.DoesNotExist:
        return Response(status=404)
    
    #Calculate on-time delivery rate(Percentage of orders delivered by the promised date)
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    on_time_orders = PurchaseOrder.objects.filter(vendor=vendor, delivery_date=F('order_date') + timedelta(days=vendor.on_time_delivery_date)).count()
    on_time_delivery_rate = (on_time_orders / total_orders)*100 if total_orders > 0 else 0

    #Calculate quality rating
    quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor).aggregate(quality_avg=Avg('quality_rating'))['quality_avg'] or 0

    #Calculate response time
    response_time_avg = PurchaseOrder.objects.filter(vendor=vendor).aggregate(response_time_avg=Avg('acknowledgement_date' - 'issue_date'))['response_time_avg'] or 0

    #Calculate fulfillment rate
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='Completed').count()
    fulfillment_rate = (fulfilled_orders / total_orders)*100 if total_orders>0 else 0

    #Construct response data
    performance_data = {
        'on_time_delivery_rate' : round(on_time_delivery_rate, 2),
        'quality_rating_avg' : round(quality_rating_avg, 2),
        'response_time_avg' : round(response_time_avg, 2),
        'fulfillment_rate' : round(fulfillment_rate, 2)
    }

    return Response(performance_data)