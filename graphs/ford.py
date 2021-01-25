import numpy as np

from typing import Dict

from graphs.dijkstra import relax, initialize_single_source

from ordenacion.binary_search import binary_search_max_dict


def ford_fulkerson(graph: Dict):
    for u in graph:
        nodo = graph[u]
        for v in nodo['capacidades']:
            nodo['flujos'][v] = 0
            graph[v]['flujos'][u] = 0
    while True:
        path, min_cap = get_shortest_path(graph)
        if len(path) > 1:
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i + 1]
                graph[u]['flujos'][v] += min_cap
                new_cap = graph[u]['capacidades'][v] - min_cap
                graph[u]['capacidades'][v] = new_cap if new_cap > 0 else np.inf
                graph[v]['flujos'][u] = -graph[u]['flujos'][v]
        else:
            break


def get_shortest_path(graph: Dict):
    modified_dijkstra(graph)
    min_cap = np.inf
    current_node = 'well'
    path = []
    while True:
        predecesor = graph[current_node]['predecesor']
        newpath = [current_node]
        newpath.extend(path)
        path = newpath
        if predecesor is None:
            break
        cap = graph[predecesor]['capacidades'][current_node]
        min_cap = cap if cap < min_cap else min_cap
        current_node = predecesor
    return path, min_cap


def modified_dijkstra(graph: Dict):
    initialize_single_source(graph, graph['source'])
    queue = [graph['source']]
    visited = []
    while queue:
        u = queue.pop()
        if u in visited:
            continue
        visited.append(u)
        for v in u['capacidades']:
            v = graph[v]
            relax(u, v, 'capacidades')
            if queue:
                i = binary_search_max_dict(queue, v['distancia'], key='distancia')
                new_queue = []
                if i is None:
                    new_queue.append(v)
                    i = -1
                else:
                    new_queue.extend(queue[:i + 1])
                    new_queue.extend([v])
                new_queue.extend(queue[i + 1:])
                queue = new_queue
            else:
                queue.append(v)


g = {
    'source': {
        'name': 'source',
        'capacidades': {
            'v1': 16,
            'v2': 13
        },
        'flujos': {}
    },
    'v1': {
        'name': 'v1',
        'capacidades': {
            'v3': 12
        },
        'flujos': {}
    },
    'v2': {
        'name': 'v2',
        'capacidades': {
            'v1': 4,
            'v4': 14
        },
        'flujos': {}
    },
    'v3': {
        'name': 'v3',
        'capacidades': {
            'v2': 9,
            'well': 20
        },
        'flujos': {}
    },
    'v4': {
        'name': 'v4',
        'capacidades': {
            'v3': 7,
            'well': 4
        },
        'flujos': {}
    },
    'well': {
        'name': 'well',
        'capacidades': {},
        'flujos': {}
    },
}

ford_fulkerson(g)
for v in g:
    print(g[v])
