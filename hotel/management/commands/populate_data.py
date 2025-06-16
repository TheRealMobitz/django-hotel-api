from django.core.management.base import BaseCommand
from hotel.models import Hotel, Room

class Command(BaseCommand):
    help = 'Populate database with sample hotel and room data'

    def handle(self, *args, **options):
        # Create sample hotels
        hotel1, created = Hotel.objects.get_or_create(
            name="Grand Hotel Tehran",
            defaults={
                'description': "Luxury 5-star hotel in the heart of Tehran",
                'address': "Valiasr Street, Tehran, Iran",
                'city': "Tehran",
                'country': "Iran",
                'phone_number': "+98-21-12345678",
                'email': "info@grandhotel-tehran.com",
                'rating': 4.7
            }
        )

        hotel2, created = Hotel.objects.get_or_create(
            name="Isfahan Heritage Hotel",
            defaults={
                'description': "Traditional Persian architecture hotel near Naqsh-e Jahan Square",
                'address': "Naqsh-e Jahan Square, Isfahan, Iran",
                'city': "Isfahan",
                'country': "Iran",
                'phone_number': "+98-31-87654321",
                'email': "reservations@isfahan-heritage.com",
                'rating': 4.5
            }
        )

        hotel3, created = Hotel.objects.get_or_create(
            name="Caspian Sea Resort",
            defaults={
                'description': "Beautiful beachfront resort on the Caspian Sea",
                'address': "Ramsar Beach, Mazandaran, Iran",
                'city': "Ramsar",
                'country': "Iran",
                'phone_number': "+98-11-22334455",
                'email': "info@caspian-resort.com",
                'rating': 4.3
            }
        )

        # Create sample rooms for each hotel
        rooms_data = [
            # Grand Hotel Tehran rooms
            {'hotel': hotel1, 'room_number': '101', 'room_type': 'single', 'price': 2500000, 'capacity': 1, 'desc': 'Elegant single room with city view'},
            {'hotel': hotel1, 'room_number': '201', 'room_type': 'double', 'price': 3500000, 'capacity': 2, 'desc': 'Spacious double room with mountain view'},
            {'hotel': hotel1, 'room_number': '301', 'room_type': 'suite', 'price': 6000000, 'capacity': 4, 'desc': 'Luxury suite with panoramic city view'},
            
            # Isfahan Heritage Hotel rooms
            {'hotel': hotel2, 'room_number': '102', 'room_type': 'single', 'price': 2000000, 'capacity': 1, 'desc': 'Traditional Persian decorated single room'},
            {'hotel': hotel2, 'room_number': '202', 'room_type': 'double', 'price': 3000000, 'capacity': 2, 'desc': 'Double room with traditional Iranian carpet'},
            {'hotel': hotel2, 'room_number': '302', 'room_type': 'deluxe', 'price': 4500000, 'capacity': 3, 'desc': 'Deluxe room with historic square view'},
            
            # Caspian Sea Resort rooms
            {'hotel': hotel3, 'room_number': '103', 'room_type': 'single', 'price': 1800000, 'capacity': 1, 'desc': 'Cozy single room with sea breeze'},
            {'hotel': hotel3, 'room_number': '203', 'room_type': 'double', 'price': 2800000, 'capacity': 2, 'desc': 'Double room with direct sea view'},
            {'hotel': hotel3, 'room_number': '303', 'room_type': 'suite', 'price': 5000000, 'capacity': 4, 'desc': 'Sea-facing suite with private balcony'},
        ]

        for room_data in rooms_data:
            Room.objects.get_or_create(
                hotel=room_data['hotel'],
                room_number=room_data['room_number'],
                defaults={
                    'room_type': room_data['room_type'],
                    'price_per_night': room_data['price'],
                    'capacity': room_data['capacity'],
                    'description': room_data['desc'],
                    'is_available': True
                }
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {Hotel.objects.count()} hotels and {Room.objects.count()} rooms')
        )
