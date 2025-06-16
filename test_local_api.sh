#!/bin/bash

# Test script for Django API endpoints
echo "Testing Django Hotel API endpoints..."

# Set base URL
BASE_URL="http://localhost:8000"

echo ""
echo "1. Testing hotel list endpoint..."
curl -X GET "${BASE_URL}/api/hotel/" -H "Content-Type: application/json"

echo ""
echo ""
echo "2. Testing user registration..."
curl -X POST "${BASE_URL}/api/auth/signup/" \
    -H "Content-Type: application/json" \
    -d '{
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "password_confirm": "testpass123"
    }'

echo ""
echo ""
echo "3. Testing user login..."
curl -X POST "${BASE_URL}/api/auth/login/" \
    -H "Content-Type: application/json" \
    -d '{
        "email": "test@example.com",
        "password": "testpass123"
    }'

echo ""
echo ""
echo "4. Testing reservation endpoint (should require auth)..."
curl -X GET "${BASE_URL}/api/reservation/" -H "Content-Type: application/json"

echo ""
echo ""
echo "API test completed!"
