from django.urls import path
from .views import HotelView, RoomsView

urlpatterns = [
    path("", HotelView.as_view(), name="list-hotels"),
    path("rooms/", RoomsView.as_view(), name="list-rooms"),
]
