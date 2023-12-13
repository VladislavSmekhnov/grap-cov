import random


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
    return all(v == 0 for v in vertex)


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


def generate_random_adjacency_matrix(n):
    adjacency_matrix = [[random.randint(0, 1)
                         for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if adjacency_matrix[i][i] == 1:
            adjacency_matrix[i][i] = 0

    for i in range(n):
        for j in range(i + 1, n):
            adjacency_matrix[j][i] = adjacency_matrix[i][j]

    return adjacency_matrix
