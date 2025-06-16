from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from hotel.models import Hotel, Room
from reservation.models import Reservation
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create admin user
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(f'Created admin user: {admin.username}')

        # Create regular users
        for i in range(5):
            username = f'user{i+1}'
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=f'{username}@example.com',
                    password='password123',
                    first_name=f'User{i+1}',
                    last_name='Test'
                )
                self.stdout.write(f'Created user: {user.username}')

        # Create hotels
        hotels_data = [
            {
                'name': 'Grand Hotel', 
                'city': 'Tehran', 
                'country': 'Iran',
                'address': '123 Main Street, Tehran',
                'phone_number': '+98-21-123-4567',
                'email': 'info@grandhotel.com',
                'description': 'Luxury hotel in downtown Tehran'
            },
            {
                'name': 'Royal Resort', 
                'city': 'Isfahan', 
                'country': 'Iran',
                'address': '456 Royal Ave, Isfahan',
                'phone_number': '+98-31-987-6543',
                'email': 'contact@royalresort.com',
                'description': 'Beautiful resort with historical views'
            },
            {
                'name': 'Beach Paradise', 
                'city': 'Kish', 
                'country': 'Iran',
                'address': '789 Beach Road, Kish Island',
                'phone_number': '+98-76-555-0123',
                'email': 'hello@beachparadise.com',
                'description': 'Beachfront hotel with amazing sea views'
            },
        ]

        for hotel_data in hotels_data:
            if not Hotel.objects.filter(name=hotel_data['name']).exists():
                hotel = Hotel.objects.create(**hotel_data)
                self.stdout.write(f'Created hotel: {hotel.name}')

                # Create rooms for each hotel
                room_types = ['single', 'double', 'suite', 'deluxe']
                for i in range(10):
                    room = Room.objects.create(
                        hotel=hotel,
                        room_number=f'{100 + i}',
                        room_type=random.choice(room_types),
                        price_per_night=random.randint(50, 300),
                        capacity=random.randint(1, 4),
                        is_available=random.choice([True, False])
                    )
                    self.stdout.write(f'Created room: {room.room_number} in {hotel.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data'))