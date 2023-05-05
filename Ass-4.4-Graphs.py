from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def count_trees(self):
        visited = {v: False for v in self.graph.keys()}
        count = 0
        for v in self.graph.keys():
            if not visited[v]:
                self.dfs(v, visited)
                count += 1
        return count
g = Graph()
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(6, 7)

count = g.count_trees()
print("Number of trees in the forest:", count)

