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
