from django.urls import include, path

from . import views


v1_url_patterns = [
    path("transactions/", views.my_view, name="index"),
]


urlpatterns = [
    path("v1/", include(v1_url_patterns)),
]
