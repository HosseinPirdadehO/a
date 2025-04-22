from Account.permissions import IsAdminRole, IsSellerRole, IsMarketerRole
from Account.serializers import (
    AdminDashboardSerializer,
    SellerDashboardSerializer,
    MarketerDashboardSerializer
)
from Account.serializers import AdminDashboardSerializer
from Account.permissions import IsAdminRole
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers import (
    AdminDashboardSerializer,
    SellerDashboardSerializer,
    MarketerDashboardSerializer
)
from Account.models import CustomUser


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        role = user.role

        if role == 'admin':
            data = {
                "total_users": CustomUser.objects.count(),
                "total_sellers": CustomUser.objects.filter(role='seller').count(),
                "total_marketers": CustomUser.objects.filter(role='marketer').count(),
                "total_buyers": CustomUser.objects.filter(role='buyer').count(),
                "active_users": CustomUser.objects.filter(status='active').count(),
                "inactive_users": CustomUser.objects.filter(status='inactive').count(),
            }
            serializer = AdminDashboardSerializer(data)
            return Response(serializer.data)

        elif role == 'seller':
            serializer = SellerDashboardSerializer(user)
            return Response(serializer.data)

        elif role == 'marketer':
            invited_users = CustomUser.objects.filter(
                operations='created', city=user.city
            ).count()
            data = {
                "message": f"سلام {user.first_name} عزیز!",
                "invited_users_count": invited_users,
                "city": user.city.name if user.city else "نا مشخص",
                "wallet_status": user.wallet_status,
            }
            serializer = MarketerDashboardSerializer(data)
            return Response(serializer.data)

        return Response({"detail": "نقش شما معتبر نیست."}, status=403)


class DashboardRedirectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role = request.user.role
        redirect_urls = {
            'admin': '/panel/admin/',
            'seller': '/panel/seller/',
            'marketer': '/panel/marketer/',
        }
        return Response({
            "dashboard_url": redirect_urls.get(role, '/')
        })


class DashboardRedirectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role = request.user.role
        if role == 'admin':
            url = '/panel/admin/'
        elif role == 'seller':
            url = '/panel/seller/'
        elif role == 'marketer':
            url = '/panel/marketer/'
        else:
            return Response({"error": "نقش نامعتبر است."}, status=400)

        return Response({"dashboard_url": url})


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        data = {
            "total_users": CustomUser.objects.count(),
            "total_sellers": CustomUser.objects.filter(role='seller').count(),
            "total_marketers": CustomUser.objects.filter(role='marketer').count(),
            "total_buyers": CustomUser.objects.filter(role='buyer').count(),
            "active_users": CustomUser.objects.filter(status='active').count(),
            "inactive_users": CustomUser.objects.filter(status='inactive').count(),
        }
        serializer = AdminDashboardSerializer(data)
        return Response(serializer.data)


class SellerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsSellerRole]

    def get(self, request):
        serializer = SellerDashboardSerializer(request.user)
        return Response(serializer.data)


class MarketerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsMarketerRole]

    def get(self, request):
        user = request.user
        invited_users = CustomUser.objects.filter(
            city=user.city, operations='created'
        ).count()
        data = {
            "message": f"سلام {user.first_name}!",
            "invited_users_count": invited_users,
            "city": user.city.name if user.city else "",
            "wallet_status": user.wallet_status
        }
        serializer = MarketerDashboardSerializer(data)
        return Response(serializer.data)
