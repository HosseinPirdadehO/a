from django.urls import path
from ..views.marketer_views import MarketerDashboardView

urlpatterns = [
    path('dashboard/', MarketerDashboardView.as_view(), name='marketer-dashboard'),
]
