from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorSerializer, PurchaseOrderSerializer
from .models import Vendor, PurchaseOrder
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
class VendorView(APIView):
    def get(self, request, id=None):
        try:
            if id is None:
                vendors = Vendor.objects.all()
                serializer = VendorSerializer(vendors, many=True)
                if vendors.exists():
                    return Response({'message': 'List of vendors retrieved successfully.','data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'No vendors found.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                vendor = Vendor.objects.get(pk=id)
                serializer = VendorSerializer(vendor)
                return Response({'message': 'Vendor details retrieved successfully.','data': serializer.data}, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'message': f'Vendor with ID {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'An error occurred while processing your request.','error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Vendor created successfully!','data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Error creating vendor.','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'An error occurred while processing your request.','error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        if not id:
            return Response({'message': 'Vendor ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            vendor = Vendor.objects.get(pk=id)
            serializer = VendorSerializer(vendor, data=request.data, partial=True)  # Allow partial updates
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Vendor details updated successfully.','data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Error updating vendor.','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return Response({'message': f'Vendor with ID {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'An error occurred while processing your request.','error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        if not id:
            return Response({'message': 'Vendor ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            vendor = Vendor.objects.get(pk=id)
            vendor.delete()
            return Response({'message': 'Vendor deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            return Response({'message': f'Vendor with ID {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'An error occurred while processing your request.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

class PurchaseOrderView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id=None):
        try:
            if id is None:
                vendor_id = request.query_params.get('vendor_id', None)
                if vendor_id:
                    purchase_orders = PurchaseOrder.objects.filter(vendor_id=vendor_id)
                else:
                    purchase_orders = PurchaseOrder.objects.all()
                serializer = PurchaseOrderSerializer(purchase_orders, many=True)
                if purchase_orders.exists():
                    return Response({'message': 'List of purchase orders retrieved successfully!','data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'No purchase orders found.'}, status=status.HTTP_204_NO_CONTENT)
            else:  # Retrieve all purchase orders or filtered by vendor_id
                purchase_order = get_object_or_404(PurchaseOrder, id=id)
                serializer = PurchaseOrderSerializer(purchase_order)
                return Response({'message': 'Purchase order details retrieved successfully!','data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'An error occurred while retrieving purchase orders.','error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = PurchaseOrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Purchase order created successfully!','data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Error creating purchase order.','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'An error occurred while creating the purchase order.','error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def put(self, request, id):
        if not id:
            return Response({'message': 'Purchase order ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            purchase_order = get_object_or_404(PurchaseOrder, id=id)
            serializer = PurchaseOrderSerializer(purchase_order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Purchase order details updated successfully.','data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Error updating purchase order.','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except PurchaseOrder.DoesNotExist:
            return Response({'message': f'Purchase order with ID {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'An error occurred while updating the purchase order.','error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        if not id:
            return Response({'message': 'Purchase order ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            purchase_order = get_object_or_404(PurchaseOrder, id=id)
            purchase_order.delete()
            return Response({'message': 'Purchase order deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrder.DoesNotExist:
            return Response({'message': f'Purchase order with ID {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({ 'message': 'An error occurred while deleting the purchase order.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=id)

            if purchase_order.status != 'pending':
                return Response({'error': 'PurchaseOrder status is not pending'}, status=400)

            purchase_order.status = 'completed'
            purchase_order.save()

            return Response({'message': 'PurchaseOrder status updated successfully'}, status=200)

        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'PurchaseOrder not found'}, status=404)


class VendorPerformanceView(APIView):
  """
  API endpoint to retrieve a vendor's performance metrics.
  """

  def get(self, request, vendor_id):
    try:
      vendor = Vendor.objects.get(pk=vendor_id)
      performance = {
          'message': 'Vendor performance retrieved successfully.', 
          'data': {
              'id': vendor.id,
              'name': vendor.name,
              'contact_details': vendor.contact_details,
              'address': vendor.address,
              'vendor_code': vendor.vendor_code,
              'on_time_delivery_rate': vendor.on_time_delivery_rate,
              'quality_rating_avg': vendor.quality_rating_avg,
              'average_response_time': vendor.average_response_time,
              'fulfillment_rate': vendor.fulfillment_rate,
              'created_at': vendor.created_at.isoformat(), 
              'updated_at': vendor.updated_at.isoformat(),
          }
      }
      return Response(performance, status=200)
    except Vendor.DoesNotExist:
      return Response({'error': 'Vendor not found'}, status=404)

class AcknowledgePurchaseOrderView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.acknowledgment_date = timezone.now() 
            purchase_order.save()
            
            return Response({"message": "Purchase order acknowledged successfully"}, status=status.HTTP_200_OK)

        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
