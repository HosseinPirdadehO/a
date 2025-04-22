from .views.auth_views import LoginAPIView
from .views.dashboard_views import DashboardRedirectView
from .views.dashboard_views import AdminDashboardView, SellerDashboardView, MarketerDashboardView
from .views.dashboard_views import (
    AdminDashboardView, SellerDashboardView, MarketerDashboardView
)
from django.urls import path
from django.urls import path, include
from django.urls import path
from Account.views import DashboardView


urlpatterns = [
    path('admin/', include('Account.urls.admin_urls')),
    path('seller/', include('Account.urls.seller_urls')),
    path('marketer/', include('Account.urls.marketer_urls')),
    path('', include('Account.urls.shared_urls')),
    path('auth/login/', LoginAPIView.as_view(), name='login-api'),


    path("dashboard/", DashboardView.as_view(), name="dashboard"),

]

urlpatterns += [
    path('panel/admin/', AdminDashboardView.as_view(), name='admin-panel'),
    path('panel/seller/', SellerDashboardView.as_view(), name='seller-panel'),
    path('panel/marketer/', MarketerDashboardView.as_view(), name='marketer-panel'),
]


urlpatterns += [
    path('panel/admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('panel/seller/', SellerDashboardView.as_view(), name='seller-dashboard'),
    path('panel/marketer/', MarketerDashboardView.as_view(),
         name='marketer-dashboard'),
]


urlpatterns += [
    path('panel/redirect/', DashboardRedirectView.as_view(),
         name='dashboard-redirect'),
]


urlpatterns += [
    path('admin/', include('Account.urls.admin_urls')),
    path('seller/', include('Account.urls.seller_urls')),
    path('me/', include('Account.urls.shared_urls')),  # یا هر فایل دیگه‌ای
]
