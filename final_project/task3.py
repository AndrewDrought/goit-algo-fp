import heapq

def create_graph(num_vertices):
    graph = {i: {} for i in range(num_vertices)}
    return graph

def add_edge(graph, u, v, weight):
    graph[u][v] = weight
    graph[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in graph}
    D[start_vertex] = 0

    heap = [(0, start_vertex)]
    while heap:
        (dist, current_vertex) = heapq.heappop(heap)
        for neighbor, neighbor_dist in graph[current_vertex].items():
            old_cost = D[neighbor]
            new_cost = D[current_vertex] + neighbor_dist
            if new_cost < old_cost:
                D[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return D

# Створюємо граф
graph = create_graph(5)


add_edge(graph, 0, 1, 2)
add_edge(graph, 0, 2, 3)
add_edge(graph, 1, 2, 1)
add_edge(graph, 1, 3, 1)
add_edge(graph, 2, 3, 1)
add_edge(graph, 3, 4, 1)

# Виконуємо алгоритм Дейкстри
distances = dijkstra(graph, 0)

print(distances)  # Виводимо найкоротші шляхи
