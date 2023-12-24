from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewSet)
router.register('productrating', views.ProductRatingViewSet)
urlpatterns=[
    # Vendors
    path('vendors/',views.VendorList.as_view() ),
    path('vendors/<int:pk>/',views.VendorDetail.as_view() ),
    # Product Categories
    path('categories/',views.CategoryList.as_view() ),
    path('categories/<int:pk>/',views.CategoryDetail.as_view() ),

     # Products
    path('products/',views.ProductList.as_view() ),
    path('products/<int:pk>/',views.ProductDetail.as_view() ),
    # Customers
    path('customers/',views.CustomerList.as_view() ),
    path('customers/<int:pk>/',views.CustomerDetail.as_view() ),
    # Order
    path('orders/',views.OrderList.as_view() ),
    path('orders/<int:pk>/',views.OrderDetail.as_view() ),

    # OrderItem
    path('order-items/',views.OrderItemList.as_view() ),
    path('order-items/<int:pk>/',views.OrderItemDetail.as_view() )
]

urlpatterns+=router.urls