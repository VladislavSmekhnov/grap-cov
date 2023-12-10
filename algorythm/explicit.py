import itertools


def graph_coverage_explicit(graph: list[list[int]]) -> list[int]:
    vertices = [i for i in range(len(graph))]
    for i in range(1, len(graph)):
        for combination in itertools.combinations(vertices, i):
            if is_graph_coverage(graph, combination):
                return combination
    return vertices


def is_graph_coverage(graph: list[list[int]], vertices: list[int]) -> bool:
    graph_tmp = [v.copy() for v in graph]
    for v in vertices:
        for i in range(len(graph)):
            graph_tmp[v][i] = graph_tmp[i][v] = 0
    return not any(any(v) for v in graph_tmp)


def graph_map_to_matrix(graph):
    n = len(graph)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            matrix[i][j] = 1
    return matrix


graph1 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

graph2 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
print(graph_coverage_explicit(graph_map_to_matrix(graph2)))
