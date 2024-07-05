from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'wallets', views.WalletViewSet)


v1_url_patterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    path("v1/", include(v1_url_patterns)),
]
