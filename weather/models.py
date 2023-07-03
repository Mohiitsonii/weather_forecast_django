from django.db import models


class WeatherForecast(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detailing_type = models.CharField(max_length=20)
    forecast_data = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weather forecast for Lat: {self.latitude}, Lon: {self.longitude}"
