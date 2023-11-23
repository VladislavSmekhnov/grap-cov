package org.example;

import java.util.ArrayList;
import java.util.List;

public class LazyAlg {
    private int[][] graph;
    int len;

    public LazyAlg(int[][] graph) {
        this.graph = graph;
        len = graph.length;
    }

    // Chose first vertex, connected to this one
    // if no edges found returns -1
    private int chooseFirstEdge(int k) {
        for (int i = 1; i < len; i++) {
            if (graph[i][k] == 1) {
                return i;
            }
        }

        return -1;
    }

    private void removeIncident(int i, int j) {
        for(int k = 0; k < len; k++) {
            graph[i][k] = 0;
            graph[k][i] = 0;
            graph[j][k] = 0;
            graph[k][j] = 0;
        }
    }

    public List<Integer> solve() {
        List<Integer> vertexCover = new ArrayList<>();

        for(int i = 0; i < len; i++) {
            int k = chooseFirstEdge(i);

            if(k == -1) {
                continue;
            }

            vertexCover.add(i);
            vertexCover.add(k);

            removeIncident(i, k);
        }

        return vertexCover;
    }
}
