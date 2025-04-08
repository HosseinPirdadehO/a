from .views import UserAccountViewSet, success_view, user_account_view, user_form_view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-accounts', UserAccountViewSet, basename='user-account')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    path('api/', include(router.urls)),
    path('user/form/<int:user_id>/', user_form_view,
         name='user_form_view'),
    path('user/account/<int:user_id>/', user_account_view,
         name='user_account_view'),
    path('success/', success_view, name='success_view'),
]
