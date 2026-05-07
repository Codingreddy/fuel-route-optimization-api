import requests
import polyline


API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImQxYTZlMDk1MjM3NzRkYTFhN2FkMGVhOGY2ZTMxMTg4IiwiaCI6Im11cm11cjY0In0="


def get_route(start_coords, end_coords):

    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [start_coords[1], start_coords[0]],
            [end_coords[1], end_coords[0]]
        ]
    }

    response = requests.post(
        url,
        json=body,
        headers=headers
    )

    data = response.json()

    print(data)

    # check route exists
    if "routes" not in data:
        return []

    encoded_geometry = data["routes"][0]["geometry"]

    route_points = polyline.decode(encoded_geometry)

    return route_points