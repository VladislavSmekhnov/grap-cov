package org.example;

import java.util.ArrayList;
import java.util.List;

public class ExplicitAlgorithm {
    private int[][] graph;

    public ExplicitAlgorithm(int[][] graph) {
        this.graph = graph;
    }

    private boolean check(List<Integer> verts) {
        var n = graph[0].length;
        var tmp = graph.clone();

        for (var v : verts) {
            for (var i = 0; i < n; i++) {
                if (tmp[v][i] == 1) {
                    tmp[v][i] = 0;
                    tmp[i][v] = 0;
                }
            }
        }


        for (var r : tmp) {
            for (var e : r) {
                if (e != 0)
                    return false;
            }
        }

        return true;
    }

    List<Integer> checkSubsets() {
        var n = graph[0].length;
        var subsets = new ArrayList<List<Integer>>();
        subsets.add(new ArrayList<>());

        var minLength = n;
        List<Integer> mvc = null;

        for (var v = 0; v < n; v++) {
            var sl = subsets.size();
            for (var i = 0; i < sl; i++) {
                var ssl = subsets.get(i).size();
                List<Integer> ss = subsets.get(i).subList(0, ssl);
                ss.add(v);
                subsets.add(ss);
            }
        }

        for (var verts : subsets) {
            var res = check(verts);

            if (res && verts.size() < minLength) {
                minLength = verts.size();
                mvc = verts;
            }
        }

        return mvc;
    }
}