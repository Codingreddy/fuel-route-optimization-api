from geopy.distance import geodesic
from .models import FuelStation


def find_best_stations(route_points, max_distance):
    """
    route_points = list of coordinates
    max_distance = max vehicle range in km
    """

    best_stations = []

    stations = FuelStation.objects.all()

    for point in route_points:

        nearby_stations = []

        for station in stations:

            station_location = (
                station.latitude,
                station.longitude
            )

            distance = geodesic(point, station_location).km

            # only stations near route
            if distance <= 100:
                nearby_stations.append(station)

        # sort by fuel price
        nearby_stations.sort(key=lambda x: x.retail_price)

        # pick cheapest
        if nearby_stations:
            best_stations.append({
                "route_point": point,
                "best_station": nearby_stations[0]
            })

    return best_stations