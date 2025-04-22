from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MarketerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'marketer':
            return Response({"detail": "دسترسی غیرمجاز."}, status=403)

        return Response({
            "message": f"سلام بازاریاب {request.user.first_name}!",
            "city": request.user.city.name if request.user.city else "نامشخص",
        })
