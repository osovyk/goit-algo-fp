import heapq

# Алгоритм Дейкстри з використанням бінарної купи
def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як "нескінченних"
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Словник для зберігання попередників
    previous_vertices = {vertex: None for vertex in graph}

    # Використання черги пріоритету для оптимізації вибору вершин
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більша за відому мінімальну, пропускаємо її
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані до сусідів поточної вершини
        for neighbor, weight_data in graph[current_vertex].items():
            weight = weight_data['weight']
            distance = current_distance + weight

            # Якщо знайдений коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                # Додаємо сусіда до черги з новою відстанню
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices

# Функція для відновлення найкоротшого шляху
def get_shortest_path(previous_vertices, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_vertices[current_node]
    path = path[::-1]
    return path

if __name__ == "__main__":
    # Створення графа
    graph = {
        'A': {'B': {'weight': 4}, 'C': {'weight': 2}},
        'B': {'C': {'weight': 5}, 'D': {'weight': 10}},
        'C': {'E': {'weight': 3}},
        'D': {'F': {'weight': 11}},
        'E': {'D': {'weight': 4}, 'F': {'weight': 2}},
        'F': {}
    }

    # Визначаємо початкову та кінцеву вершини
    start_vertex = 'A'
    goal_vertex = 'F'

    # Викликаємо алгоритм Дейкстри
    distance, previous_vertices = dijkstra(graph, start_vertex)

    # Виводимо найкоротші відстані до всіх вершин
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in distance.items():
        print(f"Відстань до {vertex}: {distance}")

    # Відновлюємо та виводимо найкоротший шлях до цільової вершини
    best_path = get_shortest_path(previous_vertices, goal_vertex)
    print(f"Найкоротший шлях від {start_vertex} до {goal_vertex}: {best_path}")
