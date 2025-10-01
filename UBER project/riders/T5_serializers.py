from rest_framework import serializers

class DriverLocationUpdateSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

class RideTrackingSerializer(serializers.Serializer):
    driver_latitude = serializers.FloatField()
    driver_longitude = serializers.FloatField()
