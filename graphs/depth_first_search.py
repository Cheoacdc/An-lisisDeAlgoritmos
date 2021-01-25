from typing import Dict, List


def dfs(graph: List[Dict]):
    for u in graph:
        u['color'] = 'white'
        u['predecesor'] = None
    time = 0
    for u in graph:
        if u['color'] == 'white':
            time = dfs_visit(graph, u, time)


def dfs_visit(graph: List[Dict], u: Dict, time: int) -> int:
    u['color'] = 'gray'
    time += 1
    u['i'] = time
    for i in u.get('vecinos', []):
        v = graph[i]
        if v['color'] == 'white':
            v['predecesor'] = graph.index(u)
            time = dfs_visit(graph, v, time)
    u['color'] = 'black'
    time += 1
    u['f'] = time
    return time


def dfs_dict(graph: Dict):
    for u in graph:
        graph[u]['color'] = 'white'
        graph[u]['predecesor'] = None
    time = 0
    for u in graph:
        u = graph[u]
        if u['color'] == 'white':
            time = dfs_visit_dict(graph, u, time)


def dfs_visit_dict(graph: Dict, u: Dict, time: int) -> int:
    u['color'] = 'gray'
    time += 1
    u['i'] = time
    for v in u.get('vecinos', []):
        v = graph[v]
        if v['color'] == 'white':
            v['predecesor'] = u['name']
            time = dfs_visit_dict(graph, v, time)
    u['color'] = 'black'
    time += 1
    u['f'] = time
    return time
