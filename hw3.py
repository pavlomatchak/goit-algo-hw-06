def dijkstra(graph, start):
  # Ініціалізація відстаней та множини невідвіданих вершин
  distances = {vertex: float('infinity') for vertex in graph}
  distances[start] = 0
  unvisited = list(graph.keys())

  while unvisited:
    # Знаходження вершини з найменшою відстанню серед невідвіданих
    current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

    # Якщо поточна відстань є нескінченністю, то ми завершили роботу
    if distances[current_vertex] == float('infinity'):
      break

    for neighbor, weight in graph[current_vertex].items():
      distance = distances[current_vertex] + weight

      # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
      if distance < distances[neighbor]:
        distances[neighbor] = distance

    # Видаляємо поточну вершину з множини невідвіданих
    unvisited.remove(current_vertex)

  return distances

graph = {
  "Афіни": {"Київ": 10},
  "Київ": {"і": 1,  "Афіни": 10},
  "і": {"Київ": 1, "Стамбул": 4},
  "Стамбул": {"і": 4, "Львів": 7, "І-Ф": 7, "Донецьк": 5},
  "Львів": {"Стамбул": 7, "І-Ф": 2},
  "І-Ф": {"Стамбул": 7, "Львів": 2, "Донецьк": 5},
  "Донецьк": {"І-Ф": 5, "Одеса": 3, "Луцьк": 8, "Стамбул": 5},
  "Одеса": {"Донецьк": 3, "Кропивницький": 4},
  "Кропивницький": {"Одеса": 4, "Суми": 6, "Луцьк": 4},
  "Луцьк": {"Кропивницький": 4, "Донецьк": 8},
  "Суми": {"Кропивницький": 6},
}

print(dijkstra(graph, 'Афіни'))
