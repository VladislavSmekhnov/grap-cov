from time import time
import networkx as nx
import numpy as np


def solve(matrix):
    adj_matrix = np.array(matrix)
    matrix_nx = nx.from_numpy_array(adj_matrix)
    return BNB(matrix_nx, 600)


# функция для удаления элементов из оптимального vc, если они не находятся в "рассматриваемом" состоянии
def removeFalse(optimalVC: list):
    return [ele for ele in optimalVC if ele[1]]


# branch and bound
def BNB(bnbGraph, timeLimit):
    # Преобразование временного лимита в целое число
    timeLimit = int(timeLimit)
    timeTaken = 0
    # Запоминаем время начала выполнения алгоритма
    startTime = time()
    # Создаем копию входного графа
    currGraph: nx.Graph = bnbGraph.copy()
    # Получаем список узлов в порядке убывания степени
    list_of_degrees = sorted(dict(currGraph.degree()).items(), reverse=True, key=lambda item: item[1])
    # Извлекаем максимальный узел и его степень
    max_node, maxDegree = list_of_degrees[0]  # кортеж (узел, степень)
    # Инициализация переменных для хранения оптимального вершинного покрытия
    optimalVC = np.array([])
    # Список текущего вершинного покрытия
    currVC = []
    # Список для хранения состояний границы (frontier)
    frontier = []
    # Верхняя граница равна числу узлов в исходном графе
    upperBound = currGraph.number_of_nodes()
    # Добавляем максимальный узел в границу
    frontier.append([max_node, False, -1, None])
    frontier.append([max_node, True, -1, None])

    # Основной цикл выполнения
    while len(frontier) != 0 and timeTaken < timeLimit:
        # Извлекаем вершину из границы
        poppedVertex, considered, parent_node, parent_node_considered = frontier.pop()
        # Обработка вершины в зависимости от того, рассматривается ли она или удаляется
        if considered:
            currGraph.remove_node(poppedVertex)
        else:
            # Удаляем соседей вершины из графа
            for elem in list(currGraph.neighbors(poppedVertex)):
                currVC.append([elem, True])
                currGraph.remove_node(elem)
        currVC.append([poppedVertex, considered])

        # Подсчет числа выбранных узлов в текущем вершинном покрытии
        count = 0
        for elem in currVC:
            if elem[1]:
                count += 1

        # Проверка, является ли текущее покрытие оптимальным
        if currGraph.number_of_edges() == 0:
            if count < upperBound:
                optimalVC = np.array(removeFalse(currVC.copy()))
                upperBound = count

            # Возврат на предыдущий уровень границы, если возможно
            if len(frontier) != 0:
                # Проверяем, была ли текущая вершина в предыдущем уровне границы
                if [frontier[-1][2], frontier[-1][3]] in currVC:
                    index = -1
                    # Ищем индекс вершины в текущем покрытии
                    for i in range(len(currVC)):
                        if currVC[i] == [frontier[-1][2], frontier[-1][3]]:
                            index = i + 1
                            break
                    # Если индекс найден, откатываем текущее состояние на предыдущий уровень
                    if index > -1:
                        while index < len(currVC):
                            currNode, currConsidered = currVC.pop()
                            currGraph.add_node(currNode)
                            currVCNodes = []
                            for i in range(len(currVC)):
                                currVCNodes.append(currVC[i][0])
                            for neigh in bnbGraph.neighbors(currNode):
                                if (neigh in currGraph.nodes()) and (neigh not in currVCNodes):
                                    currGraph.add_edge(neigh, currNode)
                # Если предыдущей вершины не было, возвращаемся к начальному состоянию
                elif frontier[-1][2] == -1 and frontier[-1][3] is None:
                    currVC.clear()
                    currGraph = bnbGraph.copy()
                # В противном случае, выводим сообщение об ошибке
                else:
                    print("Error")
        else:
            # Вычисление верхней границы для текущего состояния
            bound = currGraph.number_of_edges() / maxDegree
            bound += count
            # Если верхняя граница меньше текущей оптимальной, добавляем новые узлы в границу
            if bound < upperBound:
                poppedVertex2 = sorted(dict(currGraph.degree()).items(), reverse=True, key=lambda item: item[1])[0]
                frontier.append([poppedVertex2[0], False, poppedVertex, considered])
                frontier.append([poppedVertex2[0], True, poppedVertex, considered])
            else:
                # Возврат к предыдущему состоянию графа и вершинного покрытия, если возможно
                if len(frontier) != 0:
                    # Обратное отслеживание: Попытка восстановить предыдущее состояние вершинного покрытия
                    if [frontier[-1][2], frontier[-1][3]] in currVC:
                        # Поиск индекса вершины в текущем покрытии
                        index = -1
                        for i in range(len(currVC)):
                            if currVC[i] == [frontier[-1][2], frontier[-1][3]]:
                                index = i + 1
                                break
                        # Если индекс найден, откатываем текущее состояние на предыдущий уровень
                        if index > -1:
                            while index < len(currVC):
                                currNode, currConsidered = currVC.pop()
                                currGraph.add_node(currNode)
                                currVCNodes = []
                                # Создаем список уже выбранных узлов
                                for i in range(len(currVC)):
                                    currVCNodes.append(currVC[i][0])
                                # Восстанавливаем ребра для добавленной вершины
                                for neigh in bnbGraph.neighbors(currNode):
                                    if (neigh in currGraph.nodes()) and (neigh not in currVCNodes):
                                        currGraph.add_edge(neigh, currNode)

                    # Если предыдущей вершины не было, возвращаемся к начальному состоянию
                    elif frontier[-1][2] == -1 and frontier[-1][3] is None:
                        currVC.clear()
                        currGraph = bnbGraph.copy()
                    # В противном случае, выводим сообщение об ошибке
                    else:
                        print("Error")

        # Обновление времени выполнения
        timeTaken = time() - startTime
        # Проверка на достижение временного лимита
        if timeTaken > timeLimit:
            print("Time limit reached")

    return optimalVC
