from django.urls import path
from . import views

urlpatterns = [
    path('ride/request/', views.request_ride, name='request_ride'),
    path('ride/available/', views.available_rides, name='available_rides'),
    path('ride/accept/<int:ride_id>/', views.accept_ride, name='accept_ride'),
    path('ride/update-location/', views.update_driver_location, name='update_driver_location'),
    path('ride/track/<int:ride_id>/', views.track_ride, name='track_ride'),

    # New endpoints
    path('ride/complete/<int:ride_id>/', views.complete_ride, name='complete_ride'),
    path('ride/cancel/<int:ride_id>/', views.cancel_ride, name='cancel_ride'),
]
