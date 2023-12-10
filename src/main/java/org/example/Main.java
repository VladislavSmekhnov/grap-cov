package org.example;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        // Example graph represented as an adjacency matrix
        int[][] graph = {
                {0, 1, 1, 0},
                {1, 0, 1, 1},
                {1, 1, 0, 1},
                {0, 1, 1, 0}
        };
        var c = Greedy.greedyVC(graph);
        System.out.println(Greedy.greedyVC(graph));
    }
}