from .forms import UserForm
from django.http import HttpResponse, JsonResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework import viewsets
from .models import User, Login
from .Serializers import UserSerializer, UserAccountSerializer, LoginSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer


def user_form_view(request, user_id):
    try:
        if request.method == 'POST':
            user = get_object_or_404(User, id=user_id)
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponse("اطلاعات کاربر با موفقیت به‌روزرسانی شد!")
        else:
            user = get_object_or_404(User, id=user_id)
            form = UserForm(instance=user)
        return render(request, 'user_form.html', {'form': form})
    except User.DoesNotExist:
        return JsonResponse({'error': 'کاربر مورد نظر یافت نشد.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'مشکلی پیش آمد: {str(e)}'}, status=500)


def user_account_view(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'user_account_template.html', {'user': user})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی رخ داده است.', 'details': str(e)})


def success_view(request):
    return render(request, 'success.html')


class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LoginSerializer

    def get_queryset(self):
        try:
            return Login.objects.all()
        except Exception as e:
            return Response({"error": f"مشکلی پیش آمد: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": f"مشکلی پیش آمد: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": f"مشکلی پیش آمد: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": f"مشکلی پیش آمد: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))

    def perform_update(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))
