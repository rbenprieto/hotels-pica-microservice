from rest_framework import serializers
from .models import PaymentsReservations, Reservations


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = "__all__"


class PaymentsReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsReservations
        fields = "__all__"
