from django.shortcuts import render
from rest_framework import generics
from .models import Hotels
from .serializers import HotelsSerializer
from rest_framework.response import Response


class HotelView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer

    def get(self, request):
        query_param = request.query_params.get('id')
        hotels = self.get_queryset()
        if query_param:
            hotels= self.get_queryset().get(id=query_param)
            return Response(HotelsSerializer(hotels, many=False).data)
        return Response(HotelsSerializer(hotels, many=True).data)
    
