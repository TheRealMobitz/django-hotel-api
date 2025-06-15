from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'room', 'check_in_date', 'check_out_date', 
                   'total_price', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'check_in_date']
    search_fields = ['user__email', 'room__hotel__name', 'room__room_number']
    ordering = ['-created_at']
    readonly_fields = ['total_price', 'created_at', 'updated_at']