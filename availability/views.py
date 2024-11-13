from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Reservations, PaymentsReservations, Rooms, Hotels
from .serializers import ReservationsSerializer, PaymentsReservationsSerializer
from hotels.serializers import HotelsSerializer, RoomsSerializer
from hotels.auxiliars import validate_token


class ReservationsView(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer

    def post(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return Response({"error": "Token is required"}, status=401)
        token_parts = token.split(" ")
        token = token_parts[1] if len(token_parts) > 1 else None
        if not token:
            return Response({"error": "Token is required"}, status=401)
        if not validate_token(token):
            return Response({"error": "Invalid token"}, status=401)

        reservation = ReservationsSerializer(data=request.data)
        reservation.is_valid(raise_exception=True)
        reservation_created = reservation.save()
        return Response(ReservationsSerializer(reservation_created).data, status=201)

    def get(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return Response({"error": "Token is required"}, status=401)
        token_parts = token.split(" ")
        token = token_parts[1] if len(token_parts) > 1 else None
        if not token:
            return Response({"error": "Token is required"}, status=401)
        if not validate_token(token):
            return Response({"error": "Invalid token"}, status=401)

        reservations = self.get_queryset()
        reservations_serialized = ReservationsSerializer(reservations, many=True)
        new_reservations = []
        for reservation in reservations_serialized.data:
            payment_reservation = PaymentsReservations.objects.filter(
                reserva=reservation["id"]
            ).first()
            payment_reservation_serialized = PaymentsReservationsSerializer(
                payment_reservation
            )

            room = Rooms.objects.filter(id=reservation["habitacion"]).first()
            room_serialized = RoomsSerializer(room)

            hotel = Hotels.objects.filter(id=room.hotel_id).first()
            hotel_serialized = HotelsSerializer(hotel)

            reservation["payment"] = payment_reservation_serialized.data
            reservation["room"] = room_serialized.data
            reservation["hotel"] = hotel_serialized.data

            del reservation["payment"]["reserva"]
            del reservation["room"]["hotel"]
            new_reservations.append(reservation)

        return Response(new_reservations)


class PaymentsReservationsView(generics.CreateAPIView):
    queryset = PaymentsReservations.objects.all()
    serializer_class = PaymentsReservationsSerializer

    def post(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return Response({"error": "Token is required"}, status=401)
        token_parts = token.split(" ")
        token = token_parts[1] if len(token_parts) > 1 else None
        if not token:
            return Response({"error": "Token is required"}, status=401)
        if not validate_token(token):
            return Response({"error": "Invalid token"}, status=401)

        payment = PaymentsReservationsSerializer(data=request.data)
        payment.is_valid(raise_exception=True)
        payment_created = payment.save()
        return Response(
            PaymentsReservationsSerializer(payment_created).data, status=201
        )
