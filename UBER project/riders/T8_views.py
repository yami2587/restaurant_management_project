from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from ride.models import Ride
from .serializers import RideHistorySerializer  # make sure this exists

# Rider history API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rider_ride_history(request):
    # Filter only completed/cancelled rides for the current rider
    rides = Ride.objects.filter(
        rider=request.user,
        status__in=['COMPLETED', 'CANCELLED']
    ).order_by('-requested_at')

    # Apply pagination
    paginator = PageNumberPagination()
    paginated_rides = paginator.paginate_queryset(rides, request)
    serializer = RideHistorySerializer(paginated_rides, many=True)

    return paginator.get_paginated_response(serializer.data)


# Driver history API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def driver_ride_history(request):
    # Filter only completed/cancelled rides for the current driver
    rides = Ride.objects.filter(
        driver=request.user,
        status__in=['COMPLETED', 'CANCELLED']
    ).order_by('-requested_at')

    paginator = PageNumberPagination()
    paginated_rides = paginator.paginate_queryset(rides, request)
    serializer = RideHistorySerializer(paginated_rides, many=True)

    return paginator.get_paginated_response(serializer.data)
