# Breadth First Search

## Descripción:
* Input:
    * **G**: Una gráfica representada como lista de adyacencia.
    * **root**: El nodo a partir del cuál se realizará la búsqueda.
* Output: La gráfica con las distancias agregadas.
* Tiempo de ejecución: O(V + E)
## Código utilizado:
```python
def bfs(graph, root):
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
```