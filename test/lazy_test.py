import unittest

from algorythm.lazy import LazyAlg


class TestLazyAlg(unittest.TestCase):
    def setUp(self):
        self.graph = [[0, 1, 0, 1],
                      [1, 0, 1, 0],
                      [0, 1, 0, 1],
                      [1, 0, 1, 0]]
        self.lazy_alg = LazyAlg(self.graph)

    def test_chose_first_edge_returns_first_connected_vertex(self):
        self.assertEqual(self.lazy_alg.chose_first_edge(0), 1)

    def test_remove_incident_removes_all_incident_edges(self):
        self.lazy_alg.remove_incident(0, 1)
        for i in range(self.lazy_alg.len):
            self.assertEqual(self.lazy_alg.graph[0][i], 0)
            self.assertEqual(self.lazy_alg.graph[i][0], 0)
            self.assertEqual(self.lazy_alg.graph[1][i], 0)
            self.assertEqual(self.lazy_alg.graph[i][1], 0)

    def test_solve_returns_vertex_cover(self):
        self.assertEqual(self.lazy_alg.solve(), [0, 1, 2, 3])

    def test_solve_returns_empty_list_when_no_edges(self):
        self.lazy_alg.graph = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.lazy_alg.solve(), [])


if __name__ == '__main__':
    unittest.main()
