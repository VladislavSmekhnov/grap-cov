package org.example;

import java.util.ArrayList;
import java.util.List;

public class Greedy {

    public static List<Integer> greedyVC(int[][] inputGraph) {
        List<Integer> cover = new ArrayList<>();
        boolean valid;
        int[] numEdge;

        do {
            numEdge = countNumEdge(inputGraph);
            int m = getMaxNumEdgeIndex(numEdge);
            cover.add(m);
            valid = isValidCover(inputGraph, cover);
            System.out.println("s");
        } while (!valid);

        System.out.println(cover);
        var c = cover;
        return cover;
    }

    private static int[] countNumEdge(int[][] graph) {
        int n = graph.length;
        int[] numEdge = new int[n];

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (graph[i][j] == 1) {
                    numEdge[i]++;
                    numEdge[j]++;
                }
            }
        }

        return numEdge;
    }

    private static int getMaxNumEdgeIndex(int[] numEdge) {
        int maxIndex = 0;
        int maxNumEdge = 0;

        for (int i = 0; i < numEdge.length; i++) {
            if (numEdge[i] > maxNumEdge) {
                maxNumEdge = numEdge[i];
                maxIndex = i;
            }
        }

        return maxIndex;
    }

    private static boolean isValidCover(int[][] graph, List<Integer> cover) {
        boolean valid = true;
        int n = graph.length;
        int[] numEdge = new int[n];

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (graph[i][j] == 1) {
                    if (!cover.contains(i) && !cover.contains(j)) {
                        valid = false;
                        numEdge[i]++;
                        numEdge[j]++;
                    }
                }
            }
        }

        return valid;
    }

/*
    //возвращает индекс вершины с наибольшей степенью
    private static int getMaxDeg(int[] vertex) {
        int I = 0;
        int max = 0;

        for (int i = 0; i < vertex.length; i++) {
            if (vertex[i] > max) {
                max = vertex[i];
                I = i;
            }
        }

        return I;
    }

    //меняет значения в массиве степеней у вершин
    private static int[] countVertexDegs(int[][] graph) {
        int n = graph.length;
        int[] vertex_deg = new int[n];

        for(int i = 0; i < n; i++) {
            vertex_deg[i] = 0;

            for(int j = 0; j < n; j++) {
                if(graph[i][j] == 1) {
                    vertex_deg[i]++;
                    if(i == j) vertex_deg[i]++;
                }
            }
        }

        return vertex_deg;
    }

    //в графе все нули или нет?
    public static boolean isEmpty(int[] vertex) {
        for(int i = 0; i < vertex.length; i++) {
            if (vertex[i] != 0) {
                return false;
            }
        }

        return true;
    }

    //решение
    public static List<Integer> solve(int[][] igraph) {
        var graph = (int[][]) igraph.clone();
        List<Integer> result = new ArrayList<>();

        int n = graph.length;

        int[] vertex_deg = countVertexDegs(graph);

        int vertex;

        for(; result.size() < n && !isEmpty(vertex_deg);) {
            //жадно берем вершину с наибольшей степенью
            vertex = getMaxDeg(vertex_deg);
            result.add(vertex);

            //удаляем эту вершину из графа и из массива степеней
            for(int i = 0; i < n; i++) {
                graph[vertex][i] = graph[i][vertex] = 0;
            }

            vertex_deg = countVertexDegs(graph);
        }

        return result;
    }*/
}
