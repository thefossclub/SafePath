# safepath/utils/osrm_client.py
import requests

OSRM_URL = "http://router.project-osrm.org/route/v1/driving"

def get_osrm_edges(start_lat, start_lon, end_lat, end_lon):
    url = f"{OSRM_URL}/{start_lon},{start_lat};{end_lon},{end_lat}?overview=full&geometries=geojson"

    res = requests.get(url).json()
    routes = res.get("routes", [])
    if not routes:
        raise Exception("OSRM returned no routes")
    coords = [(lat, lon) for lon, lat in routes[0]["geometry"]["coordinates"]]
    edges = [(coords[i], coords[i+1]) for i in range(len(coords)-1)]
    return coords[0], coords[-1], edges

