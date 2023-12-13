from datetime import datetime
from algorythm import greedy, lazy, explicit,bnb
from util import generator

DATA_FOLDER_PATH = "data/"
DATA_FILES = ["1.mis", "2.mis", "3.mis", "4.mis", "5.mis"]


def print_result(n, res, start):
    print("Минимальное вершинное покрытие: ", len(res))
    print("Размер графа: ", n)
    print(f"Time: {datetime.now() - start}")


def test_alg(alg):
    for n in [10, 15, 20, 25]:
        graph = generator.generate_random_adjacency_matrix(n)
        start = datetime.now()
        res = alg.solve(graph)
        print_result(n, res, start)


def main():
    print('-' * 10, 'GREEDY ALGORYTHM TEST', '-' * 10)
    test_alg(greedy)
    print('-' * 10, 'BRANCH AND BOUND ALGORYTHM TEST', '-' * 10)
    test_alg(bnb)
    print('-' * 10, 'EXPLICIT ALGORYTHM TEST', '-' * 10)
    test_alg(explicit)


if __name__ == '__main__':
    main()
