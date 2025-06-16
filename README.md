# Django Hotel Reservation API

A comprehensive REST API for hotel reservation management built with Django REST Framework.

## 🚀 Live Demo
**Deployed API**: [Will be updated after deployment]

## Features

### 🔐 Authentication
- JWT Token-based authentication  
- User registration and login
- Admin and user role management

### 🏨 Hotel Management
- List all hotels with pagination
- View hotel details  
- Search hotels by city
- Room management per hotel

### 📋 Reservation Management
- Create new reservations
- View user reservations
- Cancel reservations
- Admin can manage all reservations

## API Endpoints

### Authentication
- `POST /api/auth/signup/` - User registration
- `POST /api/auth/login/` - User login

### User Management (Admin only)
- `GET /api/user/` - List all users
- `GET /api/user/{id}/` - Get/Update/Delete user

### Hotels & Rooms
- `GET /api/hotel/` - List hotels (with pagination)
- `GET /api/hotel/{id}/` - Hotel details
- `GET /api/hotel/{id}/room/` - Hotel rooms  
- `GET /api/room/{id}/` - Room details

### Reservations
- `GET /api/reservation/` - User reservations
- `POST /api/reservation/create/` - Create reservation
- `GET /api/reservation/{id}/` - Reservation details
- `POST /api/reservation/{id}/cancel/` - Cancel reservation

## Tech Stack
- Django 4.2.23 + Django REST Framework
- JWT Authentication
- CORS enabled
- PostgreSQL ready
- Deployment ready (Render/Railway)
