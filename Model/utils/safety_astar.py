# Model/utils/safety_astar.py
import heapq
from .safety_graph import haversine

def safe_a_star(graph, start, goal, danger_weight=3.0):
    pq = [(0, start)]
    cost = {start: 0}
    parent = {start: None}

    while pq:
        c, node = heapq.heappop(pq)

        if node == goal:
            break

        for nxt, dist in graph.get_neighbors(node):
            danger = graph.risk.get((node, nxt), 0.0)
            new_cost = c + dist + danger * danger_weight

            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                parent[nxt] = node
                heapq.heappush(pq, (new_cost, nxt))

    # reconstruct
    node = goal
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return list(reversed(path))

