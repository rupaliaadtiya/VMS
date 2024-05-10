from django.utils import timezone
from django.db.models import Avg
from procurement.models import HistoricalPerformance

def calculate_on_time_delivery_rate(vendor):
    """
    Calculates the on-time delivery rate for a vendor.
    """
    completed_orders = vendor.purchaseorder_set.filter(status='completed')

    total_completed = completed_orders.count()

    if total_completed == 0:
        return 0.0 
    current_time = timezone.now()

    on_time_orders = completed_orders.filter(
        delivery_date__gte=current_time
    )

    on_time_rate = on_time_orders.count() / total_completed

    return on_time_rate

def recalculate_average_response_time(vendor):
    """
    Recalculate the average response time for a given vendor.
    """
    acknowledged_pos = vendor.purchaseorder_set.filter(
        acknowledgment_date__isnull=False,
        issue_date__isnull=False
    )

    total_response_time = sum(
        (po.acknowledgment_date - po.issue_date).total_seconds()
        for po in acknowledged_pos
    )

    count = acknowledged_pos.count()

    if count == 0:
        vendor.average_response_time = 0.0
    else:
        vendor.average_response_time = total_response_time / count / 3600 

    vendor.save()

def recalculate_fulfillment_rate(vendor):
    """
    Recalculate the fulfillment rate for a given vendor.
    """
    total_pos = vendor.purchaseorder_set.all().count()

    completed_pos = vendor.purchaseorder_set.filter(
        status='completed',
    ).count()

    if total_pos == 0:
        vendor.fulfillment_rate = 0.0
    else:
        vendor.fulfillment_rate = completed_pos / total_pos

    vendor.save()

def recalculate_quality_rating_average(vendor):
    """
    Recalculate the quality rating average for a given vendor.
    """
    completed_pos_with_rating = vendor.purchaseorder_set.filter(
        status='completed',
        quality_rating__isnull=False
    )

    average_quality_rating = completed_pos_with_rating.aggregate(
        Avg('quality_rating')
    )['quality_rating__avg']

    if average_quality_rating is None:
        average_quality_rating = 0.0

    vendor.quality_rating_avg = average_quality_rating
    vendor.save()

def record_historical_performance(vendor):
    """
    Records a historical performance entry for a given vendor.
    """
    historical_performance = HistoricalPerformance(
        vendor=vendor,
        date=timezone.now(),  # Provide a value for 'date'
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate,
    )
    historical_performance.save()
