from collections import deque

def dfs_recursive(graph, vertex, visited=None):
  if visited is None:
    visited = set()
  visited.add(vertex)
  print(vertex, end=' ')  # Відвідуємо вершину
  for neighbor in graph[vertex]:
    if neighbor not in visited:
      dfs_recursive(graph, neighbor, visited)

def bfs_recursive(graph, queue, visited=None):
  # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
  if visited is None:
    visited = set()
  # Якщо черга порожня, завершуємо рекурсію
  if not queue:
    return
  # Вилучаємо вершину з початку черги
  vertex = queue.popleft()
  # Перевіряємо, чи відвідували раніше дану вершину
  if vertex not in visited:
    # Якщо не відвідували, друкуємо вершину
    print(vertex, end=" ")
    # Додаємо вершину до множини відвіданих вершин.
    visited.add(vertex)
    # Додаємо невідвіданих сусідів даної вершини в кінець черги.
    queue.extend(set(graph[vertex]) - visited)
  # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
  bfs_recursive(graph, queue, visited)

graph = {
  "Афіни": ["Київ"],
  "Київ": ["і",  "Афіни"],
  "і": ["Київ", "Стамбул"],
  "Стамбул": ["і", "Львів", "І-Ф", "Донецьк"],
  "Львів": ["Стамбул", "І-Ф"],
  "І-Ф": ["Стамбул", "Львів", "Донецьк"],
  "Донецьк": ["І-Ф", "Одеса", "Луцьк", "Стамбул"],
  "Одеса": ["Донецьк", "Кропивницький"],
  "Кропивницький": ["Одеса", "Суми", "Луцьк"],
  "Луцьк": ["Кропивницький", "Донецьк"],
  "Суми": ["Кропивницький"],
}

print('DFS')
dfs_recursive(graph, 'Афіни')
print('\n\nBFS')
bfs_recursive(graph, deque(['Афіни']))
