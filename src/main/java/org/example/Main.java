package org.example;

public class Main {
    public static void main(String[] args) {
        var graphReader = new GraphReader("src/main/java/org/example/data/1.mis");
        var graph = graphReader.read();
        var explicitAlgorithm = new ExplicitAlgorithm(graph);
        var res = explicitAlgorithm.checkSubsets();
        System.out.println(res);
    }
}