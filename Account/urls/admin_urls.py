from django.urls import path
from ..views.admin_views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='admin-user-list'),
]
