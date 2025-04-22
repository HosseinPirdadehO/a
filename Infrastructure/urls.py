from . import views
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet,
                basename='category')
router.register(r'brands', BrandViewSet,
                basename='brand')

urlpatterns = [
    path('api/', include(router.urls)),
    # مسیرهای مربوط به دسته‌بندی‌ها
    path('categories/', views.category_list,
         name='category_list'),
    path('categories/create/', views.create_category,
         name='create_category'),
    path('categories/edit/<int:pk>/', views.edit_category,
         name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category,
         name='delete_category'),

    # مسیرهای مربوط به برندها
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/create/', views.create_brand,
         name='create_brand'),
    path('brands/edit/<int:pk>/', views.edit_brand,
         name='edit_brand'),
    path('brands/delete/<int:pk>/', views.delete_brand,
         name='delete_brand'),
]
