from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Reservation
from .serializers import ReservationSerializer, ReservationCreateSerializer

class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).order_by('-created_at')

class ReservationDetailView(generics.RetrieveAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own reservations, admins can see all
        if self.request.user.is_staff:
            return Reservation.objects.all()
        return Reservation.objects.filter(user=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_reservation(request):
    serializer = ReservationCreateSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        reservation = serializer.save()
        return Response(
            ReservationSerializer(reservation).data, 
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def cancel_reservation(request, pk):
    try:
        if request.user.is_staff:
            reservation = get_object_or_404(Reservation, pk=pk)
        else:
            reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
        
        if reservation.status == 'cancelled':
            return Response(
                {'error': 'Reservation is already cancelled'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if reservation.status == 'completed':
            return Response(
                {'error': 'Cannot cancel completed reservation'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        reservation.status = 'cancelled'
        reservation.save()
        
        return Response(
            ReservationSerializer(reservation).data,
            status=status.HTTP_200_OK
        )
    
    except Reservation.DoesNotExist:
        return Response(
            {'error': 'Reservation not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )