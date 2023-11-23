package org.example;

import java.util.HashSet;
import java.util.Set;

public class FixedParamTractability {
    public static void main(String[] args) {
        // Example graph represented as an adjacency matrix
        int[][] graph = {
                {0, 1, 1, 0, 0},
                {1, 0, 1, 1, 1},
                {1, 1, 0, 1, 0},
                {0, 1, 1, 0, 1},
                {0, 1, 0, 1, 0}
        };

        int vertexCount = graph.length;

        // Solve the Vertex Cover problem with k = 2
        int k = 2;
        Set<Integer> vertexCover = findVertexCover(graph, k);

        if (vertexCover.isEmpty()) {
            System.out.println("No vertex cover of size " + k + " found.");
        } else {
            System.out.println("Vertex cover of size " + k + ": " + vertexCover);
        }
    }

    private static Set<Integer> findVertexCover(int[][] graph, int k) {
        Set<Integer> vertexCover = new HashSet<>();
        if (isVertexCover(graph, k, 0, vertexCover)) {
            return vertexCover;
        } else {
            return new HashSet<>(); // Return an empty set if no vertex cover is found
        }
    }

    private static boolean isVertexCover(int[][] graph, int k, int vertex, Set<Integer> vertexCover) {
        if (k == 0) {
            // Found a vertex cover of size k
            return true;
        }

        if (vertex == graph.length) {
            // Reached the end of the graph
            return false;
        }

        // Try including the current vertex in the vertex cover
        vertexCover.add(vertex);
        boolean includeVertex = isVertexCover(graph, k - 1, vertex + 1, vertexCover);
        if (includeVertex) {
            return true;
        }

        // If including the current vertex did not lead to a valid cover, try excluding it
        vertexCover.remove(vertex);
        return isVertexCover(graph, k, vertex + 1, vertexCover);
    }
}
