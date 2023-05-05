from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:
            start_vertex = queue.pop(0)
            print(start_vertex, end=" ")

            for neighbor in self.graph[start_vertex]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)
