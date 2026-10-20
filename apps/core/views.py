from django.http import JsonResponse
from django.db import connection


def health_check(request):
    """
    Simple health endpoint required by the challenge.
    Returns 200 and checks database connection.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    status_code = 200 if db_status == "connected" else 503

    return JsonResponse({
        "status": "ok" if status_code == 200 else "error",
        "database": db_status,
        "service": "ShipLens Branch Platform"
    }, status=status_code)
