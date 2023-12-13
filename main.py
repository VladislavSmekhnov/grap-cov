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


def test_algs(algs, test_sizes):
    graphs = [generator.generate_random_adjacency_matrix(n) for n in test_sizes]
    alg_time_results = defaultdict(lambda: [])
    for alg in algs:
        is_valid_time = True
        print('-' * 10, f'{alg.__name__} algorythm test', '-' * 10)
        for graph in graphs:
            if not is_valid_time:
                alg_time_results[alg].append(1500)
                continue
            graph_copy = [row.copy() for row in graph]
            time = test_alg(alg, graph_copy)
            if time > 1500:
                is_valid_time = False
                alg_time_results[alg].append(1500)
                continue
            alg_time_results[alg].append(time)
            print()
        plt.plot(test_sizes, alg_time_results[alg], label=alg.__name__)
    plt.xlabel("Размерность")
    plt.ylabel("Время (мс)")
    plt.yticks(list(plt.yticks()[0]) + [1500], list(plt.yticks()[0]) + ['>1500'])
    plt.legend()
    plt.show()


def main():
    test_algs([greedy, lazy, bnb, explicit], list(range(10, 101)))


if __name__ == '__main__':
    main()
