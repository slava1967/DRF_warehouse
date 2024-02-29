from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

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


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    @action(detail=True)
    def products(self, request, pk=None):
        warehouse = get_object_or_404(Warehouse.objects.all(), id=pk)
        prod_in_stock = warehouse.products.filter(orders__isnull=True)
        return Response(
            ProductSerializer(prod_in_stock, many=True).data
        )


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ['get', 'post', 'patch']
    serializer_class = OrderSerializer