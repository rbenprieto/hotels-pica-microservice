from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Reservations, PaymentsReservations
from .serializers import ReservationsSerializer, PaymentsReservationsSerializer


class ReservationsView(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer

    def post(self, request):
        payment = request.data["payment"] if request.data["payment"] else None
        reservation = ReservationsSerializer(data=request.data)
        reservation.is_valid(raise_exception=True)
        reservation_created = reservation.save()
        return Response(ReservationsSerializer(reservation_created).data, status=201)

    # def get(self, request):
    #     query_param = request.query_params.get("id")
    #     if query_param:
    #         reservation = self.get_queryset().get(id=query_param)

    #         return Response(ReservationsSerializer(reservation).data)
    #     else: 
    #         reservations = self.get_queryset()
    #         reservations_serialized = ReservationsSerializer(reservations, many=True)
    #         for reservation in reservations_serialized:
    #             payment_reservation = PaymentsReservations.objects.filter(reserva=reservation.pk)
    #             PaymentsReservationsSerializer(payment_reservation)
    #             if query_param:
    #             reservation = self.get_queryset().get(id=query_param)
    #             return Response(ReservationsSerializer(reservation).data)
    #     return Response(ReservationsSerializer(reservations, many=True).data)
