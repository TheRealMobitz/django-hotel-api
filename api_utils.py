from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    """Simple health check endpoint that doesn't require database access"""
    return JsonResponse({
        "status": "ok",
        "message": "Django API is running on Vercel",
        "version": "1.0.0"
    })

@csrf_exempt
@require_http_methods(["GET"])
def test_endpoint(request):
    """Test endpoint to verify Vercel deployment"""
    return JsonResponse({
        "status": "success",
        "message": "Vercel deployment is working",
        "endpoints": [
            "/api/health/",
            "/api/test/",
            "/api/hotel/",
            "/api/user/",
            "/api/reservation/",
            "/api/auth/"
        ]
    })
