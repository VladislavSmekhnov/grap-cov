def chose_first_edge(graph, k):
    for i in range(1, len(graph)):
        if graph[i][k] == 1:
            return i
    return -1

def remove_incident(graph, i, j):
    for k in range(len(graph)):
        graph[i][k] = 0
        graph[k][i] = 0
        graph[j][k] = 0
        graph[k][j] = 0

def solve(graph):
    vertex_cover = []
    for i in range(len(graph)):
        k = chose_first_edge(graph, i)
        if k == -1:
            continue
        vertex_cover.append(i)
        vertex_cover.append(k)
        remove_incident(graph, i, k)
    return vertex_cover
