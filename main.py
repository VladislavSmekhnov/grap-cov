from datetime import datetime
from util.reader import Reader
from algorythm.lazy import LazyAlg

DATA_FOLDER_PATH = "data/"
DATA_FILES = ["1.mis", "2.mis", "3.mis", "4.mis", "5.mis"]


def print_result(res, start):
    print("Минимальное вершинное покрытие:", end="")
    for v in res:
        print(f" {v if v >= 10 else ' ' + str(v)}", end="")
    print()
    print(f"Time: {datetime.now() - start}")


def test_lazy_alg():
    for file in DATA_FILES:
        graph = Reader.read(DATA_FOLDER_PATH + file)
        start = datetime.now()
        lazy = LazyAlg(graph)
        res = lazy.solve()
        print_result(res, start)


def main():
    test_lazy_alg()


if __name__ == '__main__':
    main()
