from django.contrib import admin
from django.urls import path, include

from transaction.urls import urlpatterns as transaction_url_patterns
from wallet.urls import urlpatterns as wallet_url_patterns


urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include(transaction_url_patterns)),
    path('', include(wallet_url_patterns)),
]
