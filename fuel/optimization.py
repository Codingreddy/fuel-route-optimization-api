from .models import FuelStation


MAX_RANGE_MILES = 500
MPG = 10


def optimize_fuel_stops(route_points):

    fuel_stops = []

    total_cost = 0

    # get cheapest stations
    stations = FuelStation.objects.exclude(
        retail_price=None
    ).order_by('retail_price')[:3]

    for station in stations:

        gallons_needed = MAX_RANGE_MILES / MPG

        stop_cost = (
            gallons_needed *
            float(station.retail_price)
        )

        total_cost += stop_cost

        fuel_stops.append({
            "truckstop_name": station.truckstop_name,
            "city": station.city,
            "state": station.state,
            "price_per_gallon": float(station.retail_price),
            "fuel_cost": round(stop_cost, 2),
            "latitude": station.latitude,
            "longitude": station.longitude,
        })

    return fuel_stops, round(total_cost, 2)