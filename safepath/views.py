# safepath/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.osrm_client import get_osrm_edges
from .utils.crime_loader import load_crime_data
from .utils.safety_graph import RoadGraph
from .utils.crime_scoring import summarize_crime_for_segment
from .utils.safety_astar import safe_a_star

@api_view(["GET"])
def safe_route(request):
    start_lat = float(request.GET.get("start_lat"))
    start_lon = float(request.GET.get("start_lon"))
    end_lat = float(request.GET.get("end_lat"))
    end_lon = float(request.GET.get("end_lon"))

    # 1. Load crime data
    crime_df = load_crime_data()

    # 2. Get road segments from OSRM
    start_node, goal_node, edges = get_osrm_edges(start_lat, start_lon, end_lat, end_lon)

    # 3. Build graph
    graph = RoadGraph()
    for a, b in edges:
        graph.add_edge(a, b)

    # 4. Score each segment with local crime
    for a, b in edges:
        risk = summarize_crime_for_segment(a, b, crime_df)
        graph.set_risk(a, b, risk)

    # 5. Find safe route
    safe_path = safe_a_star(graph, start_node, goal_node)

    return Response({
        "safe_path": safe_path,
        "nodes": len(graph.edges),
        "segments": len(edges)
    })

