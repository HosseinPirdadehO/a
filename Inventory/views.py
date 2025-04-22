from .Serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from .Serializers import InventorySerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Inventory
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import status, permissions

# Create your views here.
from django.shortcuts import render, redirect
from .forms import InventoryForm


def add_inventory_item(request):
    try:
        if request.method == 'POST':
            form = InventoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success_page')  # به صفحه موفقیت منتقل شوید
        else:
            form = InventoryForm()

    except Exception as e:
        # در صورت وقوع هرگونه خطا، یک پیام خطا نشان داده شود
        print(f"An error occurred: {e}")
        form = InventoryForm()

    return render(request, 'inventory.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')


#


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی آزاد

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": f"An error occurred while creating the item: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": f"An error occurred while updating the item: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": f"An error occurred while deleting the item: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# http://127.0.0.1:8000/Inventory/api/inventory/
