from . import views
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationSmsViewSet, ModalNotificationViewSet, ContentNotificationViewSet, AdvertisementNotificationViewSet

router = DefaultRouter()
router.register(r'notification-sms', NotificationSmsViewSet)
router.register(r'modal-notifications', ModalNotificationViewSet)
router.register(r'content-notifications', ContentNotificationViewSet)
router.register(r'advertisement-notifications',
                AdvertisementNotificationViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('Notif/', views.notification_sms_create,
         name='notification_sms_create'),
    path('notification-sms/create/', views.notification_sms_create,
         name='notification_sms_create'),
    path('modal-notification/create/', views.modal_notification_create,
         name='modal_notification_create'),

    path('content-notification/create/', views.content_notification_create,
         name='content_notification_create'),
    path('advertisement-notification/create/', views.advertisement_notification_create,
         name='advertisement_notification_create'),
    path('success/', views.success_page, name='success_page'),
    path('error/', views.error_page, name='error_page'),
]


# آدرس

# {
#   http: // 127.0.0.1: 8000/Notif/api
#     "notification-sms": "http://127.0.0.1:8000/Notif/apinotification-sms/",
#     "modal-notifications": "http://127.0.0.1:8000/Notif/apimodal-notifications/",
#     "content-notifications": "http://127.0.0.1:8000/Notif/apicontent-notifications/",
#     "advertisement-notifications": "http://127.0.0.1:8000/Notif/apiadvertisement-notifications/"
# }
