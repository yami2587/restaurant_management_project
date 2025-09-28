from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rider, Driver


class RiderRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Rider
        fields = ['username', 'email', 'password',
                  'phone_number', 'preferred_payment_method', 'default_pickup_location']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        # Create User with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create Rider profile
        rider = Rider.objects.create(user=user, **validated_data)
        return rider


class DriverRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Driver
        fields = ['username', 'email', 'password',
                  'phone_number', 'driver_license_number',
                  'vehicle_make', 'vehicle_model', 'number_plate']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, email=email, password=password)

        driver = Driver.objects.create(user=user, **validated_data)
        return driver
