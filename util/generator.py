import random


def generate_random_adjacency_matrix(n):
    adjacency_matrix = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if adjacency_matrix[i][i] == 1:
            adjacency_matrix[i][i] = 0

    for i in range(n):
        for j in range(i + 1, n):
            adjacency_matrix[j][i] = adjacency_matrix[i][j]

    return adjacency_matrix
