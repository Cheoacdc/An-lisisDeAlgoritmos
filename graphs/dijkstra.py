import numpy as np

from ordenacion.binary_search import binary_search_max_dict

from typing import Dict


def initialize_single_source(graph: Dict, node: Dict):
    for v in graph:
        graph[v]['distancia'] = np.inf
        graph[v]['predecesor'] = None
    node['distancia'] = 0


def relax(u: Dict, v: Dict, key: str = 'vecinos'):
    new_dist = u['distancia'] + u[key][v['name']]
    if v['distancia'] > new_dist:
        v['distancia'] = new_dist
        v['predecesor'] = u['name']


def dijkstra(graph: Dict, source: Dict):
    initialize_single_source(graph, source)
    sol = []
    queue = [source]
    visited = []
    while queue:
        u = queue.pop(0)
        if u in visited:
            continue
        sol.append(u)
        visited.append(u)
        for v in u['vecinos']:
            v = graph[v]
            relax(u, v)
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
    return sol


def bellman_ford(graph: Dict, source: Dict):
    initialize_single_source(graph, source)
    for i in range(len(graph) - 1):
        for u in graph:
            u = graph[u]
            for v in u['vecinos']:
                relax(u, graph[v])
    for u in graph:
        for v in graph[u]['vecinos']:
            if graph[v]['distancia'] > graph[u]['distancia'] + graph[u]['vecinos'][v]:
                return False
    return True


g = {
    's': {
        'name': 's',
        'vecinos': {
            't': 6,
            'y': 7
        }
    },
    't': {
        'name': 't',
        'vecinos': {
            'y': 8,
            'z': -4,
            'x': 5
        }
    },
    'x': {
        'name': 'x',
        'vecinos': {
            't': -2,
        }
    },
    'y': {
        'name': 'y',
        'vecinos': {
            'x': -3,
            'z': 9,
        }
    },
    'z': {
        'name': 'z',
        'vecinos': {
            'x': 7,
            's': 2
        }
    }
}

bellman_ford(g, g['s'])

g = {
    's': {
        'name': 's',
        'vecinos': {
            't': 10,
            'y': 5
        }
    },
    't': {
        'name': 't',
        'vecinos': {
            'y': 2,
            'x': 1
        }
    },
    'x': {
        'name': 'x',
        'vecinos': {
            'z': 4,
        }
    },
    'y': {
        'name': 'y',
        'vecinos': {
            'x': 9,
            'z': 2,
            't': 3
        }
    },
    'z': {
        'name': 'z',
        'vecinos': {
            'x': 6,
            's': 7
        }
    }
}

dijkstra(g, g['s'])
print(g)
