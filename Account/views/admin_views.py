from rest_framework.generics import ListAPIView
from ..models import CustomUser
from ..serializers import RegisterSerializer
from ..permissions import IsAdminRole


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminRole]
