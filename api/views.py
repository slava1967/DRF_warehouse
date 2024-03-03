from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import ApiUser, Product, Warehouse, Order
from api.serializers import UserSerializer, ProductSerializer, WarehouseSerializer, OrderSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['get', 'post', 'patch']
    serializer_class = UserSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'patch']
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    http_method_names = ['get']
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ['get', 'post', 'patch']
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
