import heapq

class Graph:

    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []

        self.edges[from_node].append((weight, to_node))
        self.edges[to_node].append((weight, from_node))

def dijkstra(graph, start_node):
    distances = {node: float("inf") for node in graph.edges}
    distances[start_node] = 0

    min_heap = [(0, start_node)]

    previous_nodes = {node: None for node in graph.edges}

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for weight, neighbor in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    return distances, previous_nodes

def get_shortest_path(previous_nodes, start_node, target_node):
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start_node else []

if __name__ == "__main__":
    g = Graph()

    edges_data = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "Z", 6),
        ("E", "Z", 3),
    ]

    for u, v, w in edges_data:
        g.add_edge(u, v, w)

    start = "A"
    distances, previous_nodes = dijkstra(g, start)

    print(f"Найкоротші відстані від вершини '{start}':")
    for node, distance in distances.items():
        path = get_shortest_path(previous_nodes, start, node)
        print(f"До вершини {node}: відстань = {distance}, шлях = {' -> '.join(path)}")