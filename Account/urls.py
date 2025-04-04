from . import main  # import روتر از فایل اصلی
from fastapi import APIRouter
from django.urls import path
from .views import create_or_edit_user, success_view, user_account, user_form_view

urlpatterns = [
    path('user_form/', user_form_view, name='user_form'),
    path('success/', success_view, name='success'),
    path('user/<int:user_id>/', user_account, name='user_account'),
    path('user/edit/<int:user_id>/', create_or_edit_user, name='user_edit'),
    path('user/new/', create_or_edit_user, name='user_create'),
]
