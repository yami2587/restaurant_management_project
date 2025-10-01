from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Ride

# Driver marks ride as completed
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_ride(request, ride_id):
    user = request.user
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Ensure user is the assigned driver
    try:
        driver = user.driver_profile
    except:
        return Response({"error": "Only drivers can complete rides"}, status=status.HTTP_403_FORBIDDEN)
    
    if ride.driver != driver:
        return Response({"error": "You are not assigned to this ride"}, status=status.HTTP_403_FORBIDDEN)

    if ride.status != "ONGOING":
        return Response({"error": "Ride is not ongoing"}, status=status.HTTP_400_BAD_REQUEST)

    ride.status = "COMPLETED"
    ride.save()
    return Response({"message": "Ride marked as completed."})


# Rider cancels ride
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_ride(request, ride_id):
    user = request.user
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Ensure user is the rider
    try:
        rider = user.rider_profile
    except:
        return Response({"error": "Only riders can cancel rides"}, status=status.HTTP_403_FORBIDDEN)
    
    if ride.rider != rider:
        return Response({"error": "You are not allowed to cancel this ride"}, status=status.HTTP_403_FORBIDDEN)

    if ride.status != "REQUESTED":
        return Response({"error": "Cannot cancel a ride that is already ongoing or completed."}, status=status.HTTP_400_BAD_REQUEST)

    ride.status = "CANCELLED"
    ride.save()
    return Response({"message": "Ride cancelled successfully."})
