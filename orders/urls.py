from django.conf import settings
from django.shortcuts import render
def home_view(request):
    restaurant_name = settings.RESTAURANT_NAME
    return render(request , 'home.html',{'restaurant_name': restaurant_name})