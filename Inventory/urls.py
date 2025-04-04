from .views import InventoryViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.urls import path
from . import views

app_name = 'Inventory'

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # مسیر APIها
    path('success-page/', views.success_page, name='success_page'),
    path('add-inventory/', views.add_inventory_item, name='add_inventory'),
]
