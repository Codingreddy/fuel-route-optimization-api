from rest_framework.decorators import api_view
from rest_framework.response import Response

from geopy.distance import geodesic

from .models import FuelStation
from .route_service import get_route
from .optimization import optimize_fuel_stops


@api_view(['GET'])
def fuel_stations(request):

    stations = FuelStation.objects.all()[:10]

    data = []

    for station in stations:
        data.append({
            "truckstop_name": station.truckstop_name,
            "city": station.city,
            "state": station.state,
            "price": station.retail_price,
        })

    return Response(data)


@api_view(['POST'])
def optimize_route(request):

    start = request.data.get("start")
    destination = request.data.get("destination")

    # hardcoded coordinates for demo
    start_coords = (32.7767, -96.7970)   # Dallas
    end_coords = (41.8781, -87.6298)     # Houston

    # get real route
    route_points = get_route(
        start_coords,
        end_coords
    )

    # optimize fuel stops
    fuel_stops, total_cost = optimize_fuel_stops(
        route_points
    )

    # calculate total distance
    total_distance = 0

    for i in range(1, len(route_points)):

        total_distance += geodesic(
            route_points[i - 1],
            route_points[i]
        ).miles

    return Response({
        "start": start,
        "destination": destination,
        "route_distance_miles": round(total_distance, 2),
        "fuel_needed_gallons": round(total_distance / 10, 2),
        "total_fuel_cost": total_cost,
        "fuel_stops": fuel_stops,
        "route_map": route_points[:50]
    })