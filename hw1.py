import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Афіни", "Київ", "і", "Стамбул", "Львів", "І-Ф", "Луцьк", "Донецьк", "Одеса", "Суми", "Кропивницький"])

G.add_edges_from([
  ("Афіни", "Київ"),
  ("Київ", "і"),
  ("і", "Стамбул"),
  ("Стамбул", "Львів"),
  ("Стамбул", "І-Ф"),
  ("Львів", "І-Ф"),
  ("І-Ф", "Донецьк"),
  ("Донецьк", "Одеса"),
  ("Одеса", "Кропивницький"),
  ("Кропивницький", "Суми"),
  ("Кропивницький", "Луцьк"),
  ("Донецьк", "Луцьк"),
  ("Донецьк", "Стамбул"),
])

print(f"Вершин: {G.number_of_nodes()}\n")
print(f"Ребер: {G.number_of_edges()}\n")
print(f"Центральності: {nx.degree_centrality(G)}\n")
print(f"Посередництво: {nx.betweenness_centrality(G)}\n")
print(f"Близькість: {nx.closeness_centrality(G)}")
nx.draw(G, with_labels=True)
plt.show()
