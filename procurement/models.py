from django.db import models
from django.utils import timezone
import string
import random
from django.core.validators import MinValueValidator

# Create your models here.
def generate_unique_vendor_code(prefix='VEN-'):
  while True:
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    full_code = f'{prefix}{code}'
    if not Vendor.objects.filter(vendor_code=full_code).exists():
      return full_code

def generate_unique_po_number(prefix='PO-'):
  while True:
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    full_code = f'{prefix}{code}'
    if not PurchaseOrder.objects.filter(po_number=full_code).exists():
      return full_code

class Vendor(models.Model):
  name = models.CharField(max_length=255)
  contact_details = models.TextField()
  address = models.TextField()
  vendor_code = models.CharField(max_length=50, unique=True, default=generate_unique_vendor_code)
  on_time_delivery_rate = models.FloatField(default=0.0)
  quality_rating_avg = models.FloatField(default=0.0)
  average_response_time = models.FloatField(default=0.0)
  fulfillment_rate = models.FloatField(default=0.0)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']

class PurchaseOrder(models.Model):
  po_number = models.CharField(max_length=50, unique=True, default=generate_unique_po_number)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  order_date = models.DateTimeField(auto_now_add=True)
  delivery_date = models.DateTimeField(blank=True, null=True)
  items = models.JSONField()
  quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
  STATUS_CHOICES = (
      ('pending', 'Pending'),
      ('completed', 'Completed'),
      ('canceled', 'Canceled'),
  )
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  quality_rating = models.FloatField(blank=True, null=True)
  issue_date = models.DateTimeField(blank=True, null=True)
  acknowledgment_date = models.DateTimeField(blank=True, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"PO #{self.po_number} - {self.vendor.name}"

  class Meta:
    ordering = ['-order_date']

class HistoricalPerformance(models.Model):
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  date = models.DateField()
  on_time_delivery_rate = models.FloatField()
  quality_rating_avg = models.FloatField()
  average_response_time = models.FloatField()
  fulfillment_rate = models.FloatField()
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return f"{self.vendor.name} Performance on {self.date}"

  class Meta:
    ordering = ['-date'] 
    unique_together = (('vendor', 'date'),) 


