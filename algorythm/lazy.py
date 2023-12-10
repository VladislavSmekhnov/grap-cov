class LazyAlg:
    def __init__(self, graph):
        self.graph = graph
        self.len = len(graph)

    def chose_first_edge(self, k):
        for i in range(1, self.len):
            if self.graph[i][k] == 1:
                return i
        return -1

    def remove_incident(self, i, j):
        for k in range(self.len):
            self.graph[i][k] = 0
            self.graph[k][i] = 0
            self.graph[j][k] = 0
            self.graph[k][j] = 0

    def solve(self):
        vertex_cover = []
        for i in range(self.len):
            k = self.chose_first_edge(i)
            if k == -1:
                continue
            vertex_cover.append(i)
            vertex_cover.append(k)
            self.remove_incident(i, k)
        return vertex_cover
