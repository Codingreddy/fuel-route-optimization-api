from django.urls import path
from .views import fuel_stations, optimize_route

urlpatterns = [
    path('stations/', fuel_stations),
    path('optimize-route/', optimize_route),
]