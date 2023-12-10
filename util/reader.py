import numpy as np


class Reader:
    @staticmethod
    def read(fname):
        graph = None
        with open(fname, 'r') as file:
            for line in file:
                parts = line.split(' ')
                if parts[0] == "p":
                    n = int(parts[2])
                    graph = np.zeros((n, n), dtype=int)
                elif parts[0] == "e":
                    if graph is None:
                        raise Exception("Чо за фигня? Где строка с описание количества вершин графа?")
                    i = int(parts[1]) - 1
                    j = int(parts[2]) - 1
                    graph[i][j] = graph[j][i] = 1
        return graph
