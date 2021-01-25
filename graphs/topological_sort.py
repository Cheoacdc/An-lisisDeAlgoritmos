from typing import Dict, List

from graphs.depth_first_search import dfs, dfs_dict

from ordenacion.merge_sort import merge_sort_dict


def topological_sort(graph: List[Dict]):
    dfs(graph)
    ordered = [v for v in graph]
    merge_sort_dict(ordered, key='f')
    result = []
    for v in ordered:
        aux = [v.get('name', graph.index(v))]
        aux.extend(result)
        result = aux
    print(result)


def topological_sort_dict(graph: Dict) -> List:
    dfs_dict(graph)
    ordered = [graph[v] for v in graph]
    merge_sort_dict(ordered, key='f')
    result = []
    for v in ordered:
        aux = [v['name']]
        aux.extend(result)
        result = aux
    return result


g = [
    {'name': 'undershorts', 'vecinos': [1, 7]},
    {'name': 'pants', 'vecinos': [2, 7]},
    {'name': 'belt', 'vecinos': [3]},
    {'name': 'shirt', 'vecinos': [2, 4]},
    {'name': 'tie', 'vecinos': [5]},
    {'name': 'jacket'},
    {'name': 'socks', 'vecinos': [7]},
    {'name': 'shoes'},
    {'name': 'watch'},
]
topological_sort(g)

g = {
    'undershorts': {'name': 'undershorts', 'vecinos': ['pants', 'shoes']},
    'pants': {'name': 'pants', 'vecinos': ['belt', 'shoes']},
    'belt': {'name': 'belt', 'vecinos': ['shirt']},
    'shirt': {'name': 'shirt', 'vecinos': ['belt', 'tie']},
    'tie': {'name': 'tie', 'vecinos': ['jacket']},
    'jacket': {'name': 'jacket'},
    'socks': {'name': 'socks', 'vecinos': ['shoes']},
    'shoes': {'name': 'shoes'},
    'watch': {'name': 'watch'},
}

topological_sort_dict(g)
