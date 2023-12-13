from datetime import *
from algorythm import greedy, lazy, explicit, bnb
from util import generator
import matplotlib.pyplot as plt
from collections import defaultdict


def print_result(n, res, time):
    print("Минимальное вершинное покрытие: ", len(res))
    print("Размер графа: ", n)
    print(f"Time: {time} ms")


def test_alg(alg, graph):
    start = datetime.now()
    res = alg.solve(graph)
    time = (datetime.now() - start) / timedelta(milliseconds=1)
    print_result(len(graph), res, time)
    return time


def test_algs1():
    test_sizes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    graphs = []
    for n in test_sizes:
        graphs.append(generator.generate_random_adjacency_matrix(n))
    algs = [greedy, lazy, explicit, bnb]
    alg_time_results = defaultdict(lambda: [])
    for alg in algs:
        print('-' * 10, f'{alg} algorythm test', '-' * 10)
        for graph in graphs:
            graph_copy = [row.copy() for row in graph]
            alg_time_results[alg].append(test_alg(alg, graph_copy))
            print()
    for alg in algs:
        plt.plot(test_sizes, alg_time_results[alg], label=alg)
    plt.legend()
    plt.show()


def test_algs2():
    test_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    graphs = []
    for n in test_sizes:
        graphs.append(generator.generate_random_adjacency_matrix(n))
    algs = [greedy, lazy, bnb]
    alg_time_results = defaultdict(lambda: [])
    for alg in algs:
        print('-' * 10, f'{alg} algorythm test', '-' * 10)
        for graph in graphs:
            graph_copy = [row.copy() for row in graph]
            alg_time_results[alg].append(test_alg(alg, graph_copy))
            print()
    for alg in algs:
        plt.plot(test_sizes, alg_time_results[alg], label=alg)
    plt.legend()
    plt.show()


def main():
    test_algs2()


if __name__ == '__main__':
    main()
