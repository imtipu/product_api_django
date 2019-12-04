from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.viewsets import *
# router = DefaultRouter()
# router.register('product', ProductModelViewSet)
from .views import *
urlpatterns = [
    path('products/add/', AddProduct.as_view(), name='api_add_product'),
    path('products/list/', ProductList.as_view(), name='api_list_product'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='api_product_details'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='api_product_update'),
    path('products/<int:pk>/attributes/', ProductAttributes.as_view(), name='api_product_attributes'),
    path('products/attributes/<int:pk>/update/', AttributeUpdate.as_view(), name='api_attributes_update'),
]
