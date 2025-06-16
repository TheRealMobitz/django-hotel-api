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
curl -X POST "${BASE_URL}/api/user/register/" \
    -H "Content-Type: application/json" \
    -d '{
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "password2": "testpass123",
        "first_name": "Test",
        "last_name": "User"
    }'

echo ""
echo ""
echo "3. Testing user login..."
curl -X POST "${BASE_URL}/api/user/login/" \
    -H "Content-Type: application/json" \
    -d '{
        "email": "test@example.com",
        "password": "testpass123"
    }'

echo ""
echo ""
echo "API test completed!"
