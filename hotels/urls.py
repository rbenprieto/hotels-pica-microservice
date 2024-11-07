from django.urls import path
from .views import HotelView

urlpatterns = [
    path("", HotelView.as_view(), name="hotels-list")
]