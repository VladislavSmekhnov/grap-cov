def graph_map_to_matrix(graph: map[int, list[int]]) -> list[list[int]]:
    n = len(graph)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            matrix[i][j] = 1
    return matrix
