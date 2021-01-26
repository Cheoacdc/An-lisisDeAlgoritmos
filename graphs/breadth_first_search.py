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
