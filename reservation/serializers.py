from rest_framework import serializers
from django.utils import timezone
from .models import Reservation
from hotel.serializers import RoomSerializer

class ReservationSerializer(serializers.ModelSerializer):
    room_details = RoomSerializer(source='room', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'user_email', 'room', 'room_details', 
                 'check_in_date', 'check_out_date', 'total_price', 'status', 
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'total_price', 'created_at', 'updated_at']
    
    def validate(self, attrs):
        check_in = attrs.get('check_in_date')
        check_out = attrs.get('check_out_date')
        
        if check_in and check_out:
            if check_out <= check_in:
                raise serializers.ValidationError("Check-out date must be after check-in date")
            
            if check_in < timezone.now().date():
                raise serializers.ValidationError("Check-in date cannot be in the past")
        
        return attrs

class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['room', 'check_in_date', 'check_out_date']
    
    def validate(self, attrs):
        check_in = attrs.get('check_in_date')
        check_out = attrs.get('check_out_date')
        room = attrs.get('room')
        
        if check_out <= check_in:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        
        if check_in < timezone.now().date():
            raise serializers.ValidationError("Check-in date cannot be in the past")
        
        # Check if room is available for the dates
        overlapping_reservations = Reservation.objects.filter(
            room=room,
            status__in=['pending', 'confirmed'],
            check_in_date__lt=check_out,
            check_out_date__gt=check_in
        )
        
        if overlapping_reservations.exists():
            raise serializers.ValidationError("Room is not available for the selected dates")
        
        return attrs
    
    def create(self, validated_data):
        # Calculate total price
        check_in = validated_data['check_in_date']
        check_out = validated_data['check_out_date']
        room = validated_data['room']
        
        days = (check_out - check_in).days
        total_price = room.price_per_night * days
        
        reservation = Reservation.objects.create(
            user=self.context['request'].user,
            total_price=total_price,
            **validated_data
        )
        return reservation