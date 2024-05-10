from django.db.models.signals import post_save
from django.dispatch import receiver
from procurement.models import PurchaseOrder
from procurement.utils import calculate_on_time_delivery_rate, recalculate_average_response_time, recalculate_fulfillment_rate, recalculate_quality_rating_average, record_historical_performance
import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, created, **kwargs):
    """
    Signal handler to update the on-time delivery rate when a purchase order is completed.
    """
    if instance.status == 'completed':
        new_rate = calculate_on_time_delivery_rate(instance.vendor)
        
        instance.vendor.on_time_delivery_rate = new_rate
        
        instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_on_acknowledgment(sender, instance, **kwargs):
    """
    Signal handler to update the average response time when a purchase order is acknowledged.
    """
    if instance.acknowledgment_date:
        recalculate_average_response_time(instance.vendor)

@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    """
    Signal handler to update the fulfillment rate whenever a PO is saved.
    """
    logger.info("Recalculating fulfillment rate.")
    recalculate_fulfillment_rate(instance.vendor) 

@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_average(sender, instance, **kwargs):
    """
    Signal handler to update the quality rating average upon PO completion.
    """
    if instance.status == 'completed' and instance.quality_rating is not None:
        logger.info("Purchase order completed with a quality rating. Recalculating quality rating average.")
        recalculate_quality_rating_average(instance.vendor)

@receiver(post_save, sender=PurchaseOrder)
def record_performance_on_po_completion(sender, instance, **kwargs):
    """
    Record historical performance when a purchase order is completed.
    """
    if instance.status == 'completed':
        record_historical_performance(instance.vendor)


