#!/bin/bash

# Build script for Vercel
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Running migrations..."
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Creating sample data..."
python3 manage.py populate_data