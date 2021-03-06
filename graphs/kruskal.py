from typing import Dict, List

from ordenacion.merge_sort import merge_sort_dict


def make_set(x: Dict):
    x['pointer'] = x
    x['rank'] = 0


def union(x: Dict, y: Dict):
    link(find_set(x), find_set(y))


def find_set(x: Dict):
    pointer = x['pointer']
    if pointer is not x:
        pointer = find_set(pointer)
    return pointer


def link(x: Dict, y: Dict):
    if x['rank'] > y['rank']:
        y['pointer'] = x
    else:
        x['pointer'] = y
        if x['rank'] == y['rank']:
            y['rank'] += 1


def kruskal(graph: Dict):
    sol = []
    edges = []
    for node in graph:
        make_set(graph[node])
        for vecino in graph[node]['vecinos']:
            edges.append({'u': node, 'v': vecino, 'w': graph[node]['vecinos'][vecino]})
    merge_sort_dict(edges, key='w')
    for edge in edges:
        u = graph[edge['u']]
        v = graph[edge['v']]
        if find_set(u) is not find_set(v):
            sol.append(edge)
            union(u, v)
    return sol
