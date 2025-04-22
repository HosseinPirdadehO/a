from django.urls import path, include
print("✅ Account.urls initialized")


urlpatterns = [
    path('admin/', include('Account.urls.admin_urls')),
    path('seller/', include('Account.urls.seller_urls')),
    path('marketer/', include('Account.urls.marketer_urls')),
]
