import numpy as np

from typing import Dict, List


def bfs(graph: List[Dict], root: Dict) -> None:
    for u in graph:
        if u is not root:
            u['color'] = 'white'
            u['distancia'] = np.inf
        else:
            u['color'] = 'gray'
            u['distancia'] = 0
        u['predecesor'] = None
    queue = [root]
    while queue:
        u = queue.pop(0)
        for v in u.get('vecinos', []):
            if graph[v]['color'] == 'white':
                graph[v]['color'] = 'gray'
                graph[v]['distancia'] = u['distancia'] + 1
                graph[v]['predecesor'] = graph.index(u)
                queue.append(graph[v])
        u['color'] = 'black'


def bfs_dict(graph: Dict, root: Dict) -> None:
    for u in graph:
        u = graph[u]
        if u is not root:
            u['color'] = 'white'
            u['distancia'] = np.inf
        else:
            u['color'] = 'gray'
            u['distancia'] = 0
        u['predecesor'] = None
    queue = [root]
    while queue:
        u = queue.pop(0)
        for v in u.get('vecinos', []):
            if graph[v]['color'] == 'white':
                graph[v]['color'] = 'gray'
                graph[v]['distancia'] = u['distancia'] + 1
                graph[v]['predecesor'] = u['name']
                queue.append(graph[v])
        u['color'] = 'black'


r = {'vecinos': [1, 3]}
g = [r, {'vecinos': [2]}, {}, {'vecinos': [1, 4]}, {}]
bfs(g, r)
print(g)

g = {
    '1': {'name': '1', 'vecinos': ['2', '4']},
    '2': {'name': '2', 'vecinos': ['3']},
    '3': {'name': '3'},
    '4': {'name': '4', 'vecinos': ['2', '5']},
    '5': {'name': '5'}
}
bfs_dict(g, g['1'])
print(g)
