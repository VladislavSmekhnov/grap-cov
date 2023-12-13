from datetime import *
from algorythm import greedy, lazy, explicit, bnb
from util import generator
import matplotlib.pyplot as plt


def print_result(n, res, time):
    print("Минимальное вершинное покрытие: ", len(res))
    print("Размер графа: ", n)
    print(f"Time: {time} ms")


def test_alg(alg, sizes):
    if alg == explicit:
        sizes = [5, 10, 20]
    time_results = []
    for n in sizes:
        graph = generator.generate_random_adjacency_matrix(n)
        start = datetime.now()
        res = alg.solve(graph)
        time = (datetime.now() - start) / timedelta(milliseconds=1)
        print_result(n, res, time)
        time_results.append(time)
    return time_results


def test_algs():
    sizes = [5, 10, 20, 50, 100, 200, 500]
    print('-' * 10, 'GREEDY ALGORYTHM TEST', '-' * 10)
    greedy_time_results = test_alg(greedy, sizes)
    print('-' * 10, 'BRANCH AND BOUND ALGORYTHM TEST', '-' * 10)
    test_alg(bnb, sizes)
    print('-' * 10, 'LAZY ALGORYTHM TEST', '-' * 10)
    lazy_time_results = test_alg(lazy, sizes)
    # print('-' * 10, 'EXPLICIT ALGORYTHM TEST', '-' * 10)
    # explicit_time_results = test_alg(explicit, sizes)

    # plt.plot(sizes, greedy_time_results, label='greedy')
    # plt.plot(sizes, lazy_time_results, label='lazy')
    # plt.plot(sizes, explicit_time_results, label='explicit')
    # plt.legend()
    # plt.show()


def main():
    test_algs()


if __name__ == '__main__':
    main()
