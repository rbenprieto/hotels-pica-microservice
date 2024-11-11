from django.urls import path
from .views import ReservationsView

urlpatterns = [
    path("reservation/", ReservationsView.as_view(), name="create-reservation"),
]
