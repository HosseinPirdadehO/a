from .forms import AdvertisementNotificationForm, ContentNotificationForm, ModalNotificationForm, NotificationSmsForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import NotificationSms, ModalNotification, ContentNotification, AdvertisementNotification
from .Serializers import NotificationSmsSerializer, ModalNotificationSerializer, ContentNotificationSerializer, AdvertisementNotificationSerializer

# Create your views here.


class NotificationSmsViewSet(viewsets.ModelViewSet):
    queryset = NotificationSms.objects.all()
    serializer_class = NotificationSmsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'city', 'user_group']
    # نیاز به اضافه کردن فیلدهای زمانی در مدل
    ordering_fields = ['created_at', 'title']
    # محدودیت فقط برای کاربران احراز هویت شده
    # permission_classes = [permissions.IsAuthenticated]محدود  اجازه دسترسی
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی آزاد

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "اطلاع‌رسانی با موفقیت ایجاد شد.", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"خطا در ایجاد اطلاع‌رسانی: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({"message": "اطلاع‌رسانی با موفقیت به‌روزرسانی شد.", "data": response.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"خطا در به‌روزرسانی اطلاع‌رسانی: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({"message": "اطلاع‌رسانی با موفقیت حذف شد."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": f"خطا در حذف اطلاع‌رسانی: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class ModalNotificationViewSet(viewsets.ModelViewSet):
    queryset = ModalNotification.objects.all()
    serializer_class = ModalNotificationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'province', 'city']
    # اجازه خواندن بدون احراز هویت
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]


class ContentNotificationViewSet(viewsets.ModelViewSet):
    queryset = ContentNotification.objects.all()
    serializer_class = ContentNotificationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'province', 'city', 'user_group']
    ordering_fields = ['province', 'city']
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class AdvertisementNotificationViewSet(viewsets.ModelViewSet):
    queryset = AdvertisementNotification.objects.all()
    serializer_class = AdvertisementNotificationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['province', 'city']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]


# ویو برای  نمایش تمپلیت ها


def notification_sms_create(request):
    try:
        if request.method == 'POST':
            form = NotificationSmsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('notification_sms_success')
        else:
            form = NotificationSmsForm()
        return render(request, 'NotificationSms.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"خطا در ایجاد اطلاع‌رسانی: {str(e)}"})


def modal_notification_create(request):
    try:
        if request.method == 'POST':
            form = ModalNotificationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('modal_notification_success')
        else:
            form = ModalNotificationForm()
        return render(request, 'ModalNotification.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"خطا در ایجاد اطلاع‌رسانی مودال: {str(e)}"})


def content_notification_create(request):
    try:
        if request.method == 'POST':
            form = ContentNotificationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('content_notification_success')
        else:
            form = ContentNotificationForm()
        return render(request, 'ContentNotification.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"خطا در ایجاد اطلاع‌رسانی محتوا: {str(e)}"})


def advertisement_notification_create(request):
    try:
        if request.method == 'POST':
            form = AdvertisementNotificationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('advertisement_notification_success')
        else:
            form = AdvertisementNotificationForm()
        return render(request, 'AdvertisementNotification.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'error_message': f"خطا در ایجاد تبلیغات: {str(e)}"})


def success_page(request):
    return render(request, 'success_page.html', {'message': 'عملیات با موفقیت انجام شد!'})


def error_page(request):
    return render(request, 'error.html', {'message': 'مشکلی پیش آمده است!'})
