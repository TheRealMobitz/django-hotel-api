"""
URL configuration for DjangoRestAPI4thHW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hotel.views import RoomDetailView
from api_utils import health_check, test_endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check, name='health-check'),
    path('api/test/', test_endpoint, name='test-endpoint'),
    path('api/user/', include('user.urls')),
    path('api/hotel/', include('hotel.urls')),
    path('api/reservation/', include('reservation.urls')),
    path('api/auth/', include('user.auth_urls')),
    path('api/room/<int:room_id>/', RoomDetailView.as_view(), name='room-detail'),
]