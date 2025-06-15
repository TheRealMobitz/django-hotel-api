from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Hotel, Room
from .serializers import HotelSerializer, HotelDetailSerializer, RoomSerializer, RoomDetailSerializer

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]  # Hotels can be viewed by anyone
    
    def get_queryset(self):
        queryset = Hotel.objects.all()
        city = self.request.query_params.get('city', None)
        if city:
            queryset = queryset.filter(city__icontains=city)
        return queryset.order_by('name')

class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [permissions.AllowAny]

class HotelRoomsView(generics.ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        hotel_id = self.kwargs['hotel_id']
        return Room.objects.filter(hotel_id=hotel_id, is_available=True)

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_url_kwarg = 'room_id'
    
    def get_object(self):
        room_id = self.kwargs['room_id']
        return get_object_or_404(Room, id=room_id)