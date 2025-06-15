#!/bin/bash

BASE_URL="http://localhost:8000"

echo "Testing API Endpoints..."

# Test signup
echo "1. Testing signup..."
SIGNUP_RESPONSE=$(curl -s -X POST $BASE_URL/api/auth/signup/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser2", "email": "test2@example.com", "password": "testpass123", "password_confirm": "testpass123"}')
echo $SIGNUP_RESPONSE

# Test login
echo "2. Testing login..."
LOGIN_RESPONSE=$(curl -s -X POST $BASE_URL/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "test2@example.com", "password": "testpass123"}')
echo $LOGIN_RESPONSE

# Extract access token (you'll need jq for this)
# ACCESS_TOKEN=$(echo $LOGIN_RESPONSE | jq -r '.access')

# Test hotels
echo "3. Testing hotels list..."
HOTELS_RESPONSE=$(curl -s -X GET $BASE_URL/api/hotel/)
echo $HOTELS_RESPONSE

echo "API testing completed!"
