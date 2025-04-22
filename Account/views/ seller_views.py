from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SellerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'seller':
            return Response({"detail": "شما مجاز نیستید."}, status=403)

        return Response({
            "message": f"سلام فروشنده {request.user.first_name}!",
            "wallet": request.user.wallet_status,
        })
