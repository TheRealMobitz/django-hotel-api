from django.contrib import admin
from .models import Hotel, Room

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'country', 'rating', 'created_at']
    list_filter = ['city', 'country', 'rating', 'created_at']
    search_fields = ['name', 'city', 'country']
    ordering = ['name']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_number', 'room_type', 'price_per_night', 'capacity', 'is_available']
    list_filter = ['hotel', 'room_type', 'is_available']
    search_fields = ['hotel__name', 'room_number']
    ordering = ['hotel', 'room_number']