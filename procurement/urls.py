from django.urls import path, include
from procurement import views

urlpatterns = [
    path('vendors/', views.VendorView.as_view()),
    path('vendors/<int:id>/', views.VendorView.as_view()),
    path('purchase_orders/', views.PurchaseOrderView.as_view()),
    path('purchase_orders/<int:id>/', views.PurchaseOrderView.as_view()),
    path('vendors/<int:vendor_id>/performance/', views.VendorPerformanceView.as_view()),
    path('purchase_orders/<int:po_id>/acknowledge/', views.AcknowledgePurchaseOrderView.as_view()),
]