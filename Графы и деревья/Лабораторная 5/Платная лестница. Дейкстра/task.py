]from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # _, coasts = nx.dijkstra_predecessor_and_distance(g, starting_node)
    #     for node in g.nodes:
    #         if node not in coasts:
    #             coasts[node] = float("inf")
    #
    #     return coasts

    n = len(stairway)

    if len == 1:
        return stairway[0]

    distances = [float('inf')] * (n+1)
    distances[] = 0

    predecessor = {node: None for node in g.nodes}

    queue = Pr





if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = ...  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
