from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        stack[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.dfs(i, visited, stack):
                    return True
            elif stack[i]:
                return True
        stack[v] = False
        return False

    def is_cyclic(self):
        visited = {v: False for v in self.graph.keys()}
        stack = {v: False for v in self.graph.keys()}
        for v in self.graph.keys():
            if not visited[v]:
                if self.dfs(v, visited, stack):
                    return True
        return False
        
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

is_cyclic = g.is_cyclic()
if is_cyclic:
    print("The graph contains a cycle")
else:
    print("The graph does not contain a cycle")

            