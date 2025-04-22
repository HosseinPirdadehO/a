from Account.views.dashboard_views import DashboardView
from Account.views import DashboardView
from django.urls import path
from ..views.shared_views import MeView
from ..urls_a import urlpatterns

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
