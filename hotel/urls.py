from django.urls import path
from . import views

urlpatterns = [
    path('', views.HotelListView.as_view(), name='hotel-list'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('<int:hotel_id>/room/', views.HotelRoomsView.as_view(), name='hotel-rooms'),
]