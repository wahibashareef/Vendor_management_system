from django.urls import path
from . import views

urlpatterns = [
    path('', views.getVendor),
    path('api/vendor/', views.addVendor),
    path('api/vendor/<id>', views.getSingleVendor),
    path('api/vendor/<id>/update', views.updateVendor),
    path('api/vendor/<id>/delete', views.deleteVendor),
    path('api/purchase_orders', views.getOrders),
    path('api/purchase_order', views.purchaseOrder),
    path('api/purchase_order/<id>', views.getSingleOrder),
    path('api/purchase_order/<id>/update', views.updateOrder),
    path('api/purchase_order/<id>/delete', views.deleteOrder),
    path('api/vendors/<id>/performance', views.get_vendor_performance),
]
