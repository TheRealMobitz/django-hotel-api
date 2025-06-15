from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReservationListView.as_view(), name='reservation-list'),
    path('create/', views.create_reservation, name='reservation-create'),
    path('<int:pk>/', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('<int:pk>/cancel/', views.cancel_reservation, name='reservation-cancel'),
]