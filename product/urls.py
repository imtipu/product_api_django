from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from product.viewsets import *

router = DefaultRouter()
router.register('products', ProductModelViewSet)
nested_router = routers.NestedDefaultRouter(router, 'products', lookup='products')
nested_router.register('attributes', ProductAttributeViewSet, base_name='products-attributes')

# router.register('products/<int:pk>/attributes', ProductAttributeViewSet, basename='product_attributes')
from .views import *
urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    # path('products/add/', AddProduct.as_view(), name='api_add_product'),
    # path('products/list/', ProductList.as_view(), name='api_list_product'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='api_product_details'),
    # path('products/<int:pk>/update/', ProductUpdate.as_view(), name='api_product_update'),
    # path('products/<int:pk>/attributes/', ProductAttributes.as_view(), name='api_product_attributes'),
    # path('products/attributes/<int:pk>/update/', AttributeUpdate.as_view(), name='api_attributes_update'),
]
