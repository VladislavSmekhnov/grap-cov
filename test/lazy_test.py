import unittest

from algorythm import lazy


class TestLazyAlg(unittest.TestCase):
    def setUp(self):
        self.graph = [[0, 1, 0, 1],
                      [1, 0, 1, 0],
                      [0, 1, 0, 1],
                      [1, 0, 1, 0]]

    def test_chose_first_edge_returns_first_connected_vertex(self):
        self.assertEqual(lazy.chose_first_edge(self.graph, 0), 1)

    def test_remove_incident_removes_all_incident_edges(self):
        lazy.remove_incident(self.graph, 0, 1)
        for i in range(len(self.graph)):
            self.assertEqual(self.graph[0][i], 0)
            self.assertEqual(self.graph[i][0], 0)
            self.assertEqual(self.graph[1][i], 0)
            self.assertEqual(self.graph[i][1], 0)

    def test_solve_returns_vertex_cover(self):
        self.assertEqual(lazy.solve(self.graph), [0, 1, 2, 3])

    def test_solve_returns_empty_list_when_no_edges(self):
        self.graph = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(lazy.solve(self.graph), [])


if __name__ == '__main__':
    unittest.main()
