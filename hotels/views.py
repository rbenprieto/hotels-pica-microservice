from django.shortcuts import render
from rest_framework import generics
from .models import Hotels, Rooms
from .serializers import HotelsSerializer, RoomsSerializer
from rest_framework.response import Response


class HotelView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer

    def get(self, request):
        query_param = request.query_params.get("id")
        hotels = self.get_queryset()
        if query_param:
            hotel = self.get_queryset().get(id=query_param)
            return Response(HotelsSerializer(hotel).data)
        return Response(HotelsSerializer(hotels, many=True).data)


class RoomsView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

    def get(self, request):
        query_param = request.query_params.get("id")
        rooms = self.get_queryset()
        if query_param:
            room = self.get_queryset().get(id=query_param)
            return Response(RoomsSerializer(room).data)
        return Response(RoomsSerializer(rooms, many=True).data)
