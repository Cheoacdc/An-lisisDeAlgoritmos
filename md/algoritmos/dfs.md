# Depth First Search

## Descripción:
* Input: Una gráfica **G** representada como lista de adyacencia.
* Output: La gráfica con el tiempo de entrada y tiempo de salida de cada nodo.
* Tiempo de ejecución: O(V + E)
## Código utilizado:
```python
def dfs(graph):
    for u in graph:
        u['color'] = 'white'
        u['predecesor'] = None
    time = 0
    for u in graph:
        if u['color'] == 'white':
            time = dfs_visit(graph, u, time)


def dfs_visit(graph, u, time):
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
```