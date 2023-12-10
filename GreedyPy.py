def get_max_deg(vertex):
    I = 0
    max_deg = 0
    for i in range(len(vertex)):
        if vertex[i] > max_deg:
            max_deg = vertex[i]
            I = i
    return I

def count_vertex_degs(graph):
    n = len(graph)
    vertex_deg = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                vertex_deg[i] += 1
                if i == j:
                    vertex_deg[i] += 1
    return vertex_deg

def is_empty(vertex):
    for i in range(len(vertex)):
        if vertex[i] != 0:
            return False
    return True

def solve(graph):
    result = []

    n = len(graph)

    vertex_deg = count_vertex_degs(graph)

    while len(result) < n and not is_empty(vertex_deg):
        vertex = get_max_deg(vertex_deg)
        result.append(vertex)

        for i in range(n):
            graph[vertex][i] = graph[i][vertex] = 0
        
        vertex_deg = count_vertex_degs(graph)

    return result

'''graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]]'''

'''graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]
'''

'''graph = [
    [0, 1],
    [1, 0]
]'''

graph =[[0, 1, 1, 0, 0],
 [1, 0, 1, 1, 0],
 [1, 1, 0, 0, 1],
 [0, 1, 0, 0, 1],
 [0, 0, 1, 1, 0]]


result = solve(graph)
print(result)

'''class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = [[] for _ in range(vertices)]
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def minVertexCover(self):
        visited = [False] * self.vertices
        cover = []

        for u in range(self.vertices):
            if not visited[u]:
                for v in self.adjList[u]:
                    if not visited[v]:
                        visited[u] = True
                        visited[v] = True
                        cover.append(u)
                        cover.append(v)
                        break
        
        return cover

if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 0)
    graph = Graph(5)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 5)
    graph.addEdge(5, 2)

    result = graph.minVertexCover()
    print("Minimum Vertex Cover:", result)'''