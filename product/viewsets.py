from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import filters as rest_filters

from .models import *
from .serializers import *


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny, ]

    # def post(self, reques= AttributeVariantsSerializer(data=request.data)t):
    #     variant_serializer