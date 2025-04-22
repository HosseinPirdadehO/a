from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from Account.models import CustomUser


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            role = user.role
            if role == 'admin':
                dashboard_url = '/panel/admin/'
            elif role == 'seller':
                dashboard_url = '/panel/seller/'
            elif role == 'marketer':
                dashboard_url = '/panel/marketer/'
            else:
                dashboard_url = '/panel/unknown/'

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "dashboard_url": dashboard_url,
                "role": role,
                "full_name": f"{user.first_name} {user.last_name}"
            }, status=status.HTTP_200_OK)

        return Response({"error": "نام کاربری یا رمز عبور اشتباه است."},
                        status=status.HTTP_401_UNAUTHORIZED)
