# safepath/utils/safety_graph.py
from collections import defaultdict
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    h = (
        math.sin(d_lat/2)**2 +
        math.cos(math.radians(lat1)) *
        math.cos(math.radians(lat2)) *
        math.sin(d_lon/2)**2
    )
    return 2 * R * math.asin(math.sqrt(h)) * 1000  # meters

class RoadGraph:
    def __init__(self):
        self.edges = defaultdict(list)      # node → [(node2, dist)]
        self.risk = {}                      # (node1,node2) → risk (0–1)

    def add_edge(self, a, b):
        dist = haversine(a[0], a[1], b[0], b[1])
        self.edges[a].append((b, dist))
        self.edges[b].append((a, dist))

    def set_risk(self, a, b, value):
        self.risk[(a, b)] = value
        self.risk[(b, a)] = value

    def get_neighbors(self, node):
        return self.edges[node]


