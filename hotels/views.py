from django.shortcuts import render, get_object_or_404
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
        hotel_query_param = request.query_params.get("hotel")
        rooms = self.get_queryset()
        if query_param:
            room = get_object_or_404(Rooms, id=query_param)
            return Response(RoomsSerializer(room).data)
        if hotel_query_param:
            rooms = self.get_queryset().filter(hotel=hotel_query_param)
            return Response(RoomsSerializer(rooms, many=True).data)
        return Response(RoomsSerializer(rooms, many=True).data)
