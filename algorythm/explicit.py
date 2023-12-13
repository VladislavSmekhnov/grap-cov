import itertools


def solve(graph: list[list[int]]) -> list[int]:
    vertices = [i for i in range(len(graph))]
    for i in range(1, len(graph)):
        for combination in itertools.combinations(vertices, i):
            if is_graph_coverage(graph, combination):
                return list(combination)
    return vertices


def is_graph_coverage(graph: list[list[int]], vertices: list[int]) -> bool:
    graph_tmp = [v.copy() for v in graph]
    for v in vertices:
        for i in range(len(graph)):
            graph_tmp[v][i] = graph_tmp[i][v] = 0
    return not any(any(v) for v in graph_tmp)
