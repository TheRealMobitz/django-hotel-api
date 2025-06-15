from rest_framework import serializers
from .models import Hotel, Room

class HotelSerializer(serializers.ModelSerializer):
    rooms_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'address', 'city', 'country', 
                 'phone_number', 'email', 'rating', 'created_at', 'rooms_count']
        read_only_fields = ['id', 'created_at']
    
    def get_rooms_count(self, obj):
        return obj.rooms.count()

class HotelDetailSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()
    
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'address', 'city', 'country', 
                 'phone_number', 'email', 'rating', 'created_at', 'rooms']
        read_only_fields = ['id', 'created_at']
    
    def get_rooms(self, obj):
        rooms = obj.rooms.filter(is_available=True)
        return RoomSerializer(rooms, many=True).data

class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)
    
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'hotel_name', 'room_number', 'room_type', 
                 'price_per_night', 'capacity', 'description', 'is_available']
        read_only_fields = ['id']

class RoomDetailSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'room_number', 'room_type', 'price_per_night', 
                 'capacity', 'description', 'is_available']
        read_only_fields = ['id']