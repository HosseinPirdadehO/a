from .serializers import (
    AdminDashboardSerializer,
    SellerDashboardSerializer,
    MarketerDashboardSerializer
)
from .permissions import IsAdminRole, IsSellerRole, IsMarketerRole
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsAdminRole
from .models import CustomUser
from rest_framework.generics import ListAPIView
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import RegisterSerializer, AdminDashboardSerializer
from Account.models import CustomUser


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "ثبت‌نام با موفقیت انجام شد.",
                "user": {
                    "username": user.username,
                    "full_name": f"{user.first_name} {user.last_name}",
                    "phone": user.phone_number,
                    "role": user.role,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = RegisterSerializer(request.user)
        return Response(serializer.data)


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminRole]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "با موفقیت خارج شدید."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": " از قبل خارج شده‌اید."}, status=status.HTTP_400_BAD_REQUEST)


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        return Response({
            "total_users": CustomUser.objects.count(),
            "total_sellers": CustomUser.objects.filter(role='seller').count(),
            "total_marketers": CustomUser.objects.filter(role='marketer').count()
        })


class MarketerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsMarketerRole]

    def get(self, request):
        return Response({
            "message": f"سلام {request.user.first_name} جان!",
            "city": request.user.city.name if request.user.city else "نا مشخص",
            # فرض بر اینکه لیست کاربران جذب‌شده رو داریم
            "invited_users_count": CustomUser.objects.filter(
                operations='created', city=request.user.city
            ).count()
        })


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        total_users = CustomUser.objects.count()
        total_sellers = CustomUser.objects.filter(role='seller').count()
        total_marketers = CustomUser.objects.filter(role='marketer').count()
        total_buyers = CustomUser.objects.filter(role='buyer').count()
        active_users = CustomUser.objects.filter(status='active').count()
        inactive_users = CustomUser.objects.filter(status='inactive').count()

        data = {
            'total_users': total_users,
            'total_sellers': total_sellers,
            'total_marketers': total_marketers,
            'total_buyers': total_buyers,
            'active_users': active_users,
            'inactive_users': inactive_users,
        }

        serializer = AdminDashboardSerializer(data)
        return Response(serializer.data)


class RoleBasedDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == 'admin':
            total_users = CustomUser.objects.count()
            total_sellers = CustomUser.objects.filter(role='seller').count()
            total_marketers = CustomUser.objects.filter(
                role='marketer').count()
            total_buyers = CustomUser.objects.filter(role='buyer').count()
            active_users = CustomUser.objects.filter(status='active').count()
            inactive_users = CustomUser.objects.filter(
                status='inactive').count()

            serializer = AdminDashboardSerializer(data={
                "total_users": total_users,
                "total_sellers": total_sellers,
                "total_marketers": total_marketers,
                "total_buyers": total_buyers,
                "active_users": active_users,
                "inactive_users": inactive_users,
            })
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)

        elif user.role == 'seller':
            serializer = SellerDashboardSerializer(user)
            return Response(serializer.data)

        elif user.role == 'marketer':
            # اینجا بعدا میشه دیتا از مدل‌های دیگه هم آورد
            serializer = MarketerDashboardSerializer(data={
                "message": "خوش آمدید بازاریاب عزیز!",
                "invited_users_count": 0,  # فرضاً بعداً از مدل دعوت شده‌ها
                "city": user.city.name if user.city else "نامشخص",
                "wallet_status": user.wallet_status,
            })
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)

        return Response({"detail": "نقش کاربر نامعتبر است."}, status=400)


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == 'admin':
            total_users = CustomUser.objects.count()
            total_sellers = CustomUser.objects.filter(role='seller').count()
            total_marketers = CustomUser.objects.filter(
                role='marketer').count()
            total_buyers = CustomUser.objects.filter(role='buyer').count()
            active_users = CustomUser.objects.filter(status='active').count()
            inactive_users = CustomUser.objects.filter(
                status='inactive').count()

            data = {
                "total_users": total_users,
                "total_sellers": total_sellers,
                "total_marketers": total_marketers,
                "total_buyers": total_buyers,
                "active_users": active_users,
                "inactive_users": inactive_users
            }

            serializer = AdminDashboardSerializer(data)
            return Response(serializer.data)

        elif user.role == 'seller':
            serializer = SellerDashboardSerializer(user)
            return Response(serializer.data)

        elif user.role == 'marketer':
            invited_users = CustomUser.objects.filter(
                status='active', city=user.city).count()
            data = {
                "message": "به داشبورد مارکتر خوش آمدید!",
                "invited_users_count": invited_users,
                "city": user.city.name if user.city else "نامشخص",
                "wallet_status": user.wallet_status
            }
            serializer = MarketerDashboardSerializer(data)
            return Response(serializer.data)

        return Response({"detail": "نقش شما شناسایی نشد."}, status=403)
