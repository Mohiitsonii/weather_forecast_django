from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.utils import timezone  # Add this import
from datetime import timedelta
from django.conf import settings
from .models import WeatherForecast
from .utils import get_weather_forecast


@require_GET
def weather_forecast(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    detailing_type = request.GET.get('detailing_type')

    try:
        weather_obj = WeatherForecast.objects.get(
            latitude=lat,
            longitude=lon,
            detailing_type=detailing_type,
            last_updated__gte=(
                timezone.now() - timedelta(minutes=settings.CACHE_EXPIRY_MINUTES))
        )
        forecast_data = weather_obj.forecast_data
    except WeatherForecast.DoesNotExist:
        forecast_data = get_weather_forecast(lat, lon, detailing_type)
        weather_obj = WeatherForecast(
            latitude=lat,
            longitude=lon,
            detailing_type=detailing_type,
            forecast_data=forecast_data
        )
        weather_obj.save()

    return JsonResponse(forecast_data)
