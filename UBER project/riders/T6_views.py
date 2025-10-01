from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Ride
from .serializers import RideRequestSerializer, RideAcceptSerializer
from users.models import Rider, Driver
from .serializers import DriverLocationUpdateSerializer, RideTrackingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_ride(request):
    user = request.user
    try:
        rider = user.rider_profile
    except:
        return Response({"error": "Only riders can request rides"}, status=status.HTTP_403_FORBIDDEN)

    serializer = RideRequestSerializer(data=request.data)
    if serializer.is_valid():
        ride = serializer.save(rider=rider)
        return Response({"message": "Ride requested", "ride_id": ride.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_rides(request):
    user = request.user
    try:
        driver = user.driver_profile
    except:
        return Response({"error": "Only drivers can view available rides"}, status=status.HTTP_403_FORBIDDEN)
    
    rides = Ride.objects.filter(status='REQUESTED')
    serializer = RideRequestSerializer(rides, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_ride(request, ride_id):
    user = request.user
    try:
        driver = user.driver_profile
    except:
        return Response({"error": "Only drivers can accept rides"}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if ride.status != 'REQUESTED':
        return Response({"error": "Ride already accepted or not available"}, status=status.HTTP_400_BAD_REQUEST)

    ride.driver = driver
    ride.status = 'ONGOING'
    ride.save()
    return Response({"message": f"Ride {ride.id} accepted by {driver.user.username}"})

# Driver updates their live location
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_driver_location(request):
    user = request.user
    try:
        driver = user.driver_profile
    except:
        return Response({"error": "Only drivers can update location"}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = DriverLocationUpdateSerializer(data=request.data)
    if serializer.is_valid():
        driver.current_latitude = serializer.validated_data['latitude']
        driver.current_longitude = serializer.validated_data['longitude']
        driver.save()
        return Response({"message": "Location updated"})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
##
#
#
#for t 6
#
# Rider fetches the current location of the driver
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def track_ride(request, ride_id):
    user = request.user
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"}, status=status.HTTP_404_NOT_FOUND)

    # Ensure only the rider who booked can track
    try:
        rider = user.rider_profile
    except:
        return Response({"error": "Only riders can track rides"}, status=status.HTTP_403_FORBIDDEN)

    if ride.rider != rider:
        return Response({"error": "You are not allowed to track this ride"}, status=status.HTTP_403_FORBIDDEN)
    
    if ride.status != 'ONGOING' or not ride.driver:
        return Response({"error": "Ride not started or driver not assigned yet"}, status=status.HTTP_400_BAD_REQUEST)

    data = {
        "driver_latitude": ride.driver.current_latitude,
        "driver_longitude": ride.driver.current_longitude
    }
    serializer = RideTrackingSerializer(data)
    return Response(serializer.data)