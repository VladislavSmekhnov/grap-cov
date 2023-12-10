from datetime import datetime
from util.reader import Reader
from algorythm.lazy import LazyAlg
from algorythm import greedy
from util import generator

DATA_FOLDER_PATH = "data/"
DATA_FILES = ["1.mis", "2.mis", "3.mis", "4.mis", "5.mis"]


def print_result(n, res, start):
    print("Минимальное вершинное покрытие: ", len(res))
    print("Размер графа: ", n)
    print(f"Time: {datetime.now() - start}")


def test_lazy_alg():
    for n in [10, 50, 100, 200, 500, 1000]:
        graph = generator.generate_random_adjacency_matrix(n)
        start = datetime.now()
        lazy = LazyAlg(graph)
        res = lazy.solve()
        print_result(n, res, start)

def test_greedy_alg():
    for n in [10, 50, 100, 200, 500, 1000]:
        graph = generator.generate_random_adjacency_matrix(n)
        start = datetime.now()
        res = greedy.solve(graph)
        print_result(n, res, start)

def main():
     test_lazy_alg()
    # test_greedy_alg()
    


if __name__ == '__main__':
    main()
