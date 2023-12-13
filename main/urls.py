from django.urls import path
from . import views
urlpatterns=[
    # Vendors
    path('vendors/',views.VendorList.as_view() ),
    path('vendors/<int:pk>/',views.VendorDetail.as_view() ),
    # Products
    path('products/',views.ProductList.as_view() ),
    path('products/<int:pk>/',views.ProductDetail.as_view() ),
    # Customers
    path('customers/',views.CustomerList.as_view() ),
    path('customers/<int:pk>/',views.CustomerDetail.as_view() )
]