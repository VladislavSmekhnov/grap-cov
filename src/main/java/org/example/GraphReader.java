package org.example;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;
import java.util.logging.Logger;

public class GraphReader {

    private final String filename;
    private final Logger logger = Logger.getLogger(getClass().getName());

    public GraphReader(String filename) {
        this.filename = filename;
    }
    
    int[][] read() {
        try (var scanner = new Scanner(Path.of(filename))) {
            scanner.next();
            scanner.next();
            var vNum = scanner.nextInt();
            var eNum = scanner.nextInt();
            var graph = new int[vNum][vNum];
            for (int i = 0; i < eNum; i++) {
                scanner.next();
                var from = scanner.nextInt();
                var to = scanner.nextInt();
                graph[from - 1][to - 1] = 1;
                graph[to - 1][from - 1] = 1;
            }
            return graph;
        } catch (IOException e) {
            logger.warning("""
                    сколько людей из нас сначала пытаются развязать пакет
                    а потом психуют и забирают документы из универа?
                    """);
            throw new RuntimeException(e);
        }
    }
}
