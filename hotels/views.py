from django.shortcuts import render
from rest_framework import generics
from .models import Hotels
from .serializers import HotelsSerializer


class HotelView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
