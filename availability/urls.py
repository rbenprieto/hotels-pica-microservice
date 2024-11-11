from django.urls import path
from .views import ReservationsView, PaymentsReservationsView


urlpatterns = [
    path("reservation/", ReservationsView.as_view(), name="reservation"),
    path("reservation/pay/", PaymentsReservationsView.as_view(), name="payment-reservation"),
]
