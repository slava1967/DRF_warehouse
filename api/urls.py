from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, ProductModelViewSet, WarehouseModelViewSet, OrderModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register("products", ProductModelViewSet)
router.register("warehouses", WarehouseModelViewSet)
router.register("orders", OrderModelViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
