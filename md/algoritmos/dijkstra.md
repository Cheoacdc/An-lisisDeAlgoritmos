# Dijkstra

## Descripción:
Con este algoritmo se busca la menor distancia a todos los nodos desde cierto nodo. También se asignan predecesores a cada uno para poder construir el camino más corto.
Este algoritmo, a diferencia de **Bellman Ford**, no permite pesos negativos en las aristas de la gráfica.
* Input:
    * **graph**: Una gráfica representada como lista de adyacencia.
    * **source**: El nodo a partir del cual se asignarán las distancias.
* Output: La gráfica con las distancias desde *source* a cada nodo.
* Tiempo de ejecución: La implementación en este programa es de O(V(V + lgV)), sin embargo con Fibonacci Heaps se puede conseguir un tiempo de O(VlgV + E).
## Código utilizado:
### Función **Dijkstra**
Esta es la función principal del algoritmo. Se apoya de dos funciones que comparte con el algoritmo **Bellman Ford**. Además, se utiliza **Binary Search** para evitar reordenar por completo la *queue*.
```python
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
```
### Funciones de apoyo
```python
def initialize_single_source(graph, node):
    for v in graph:
        graph[v]['distancia'] = np.inf
        graph[v]['predecesor'] = None
    node['distancia'] = 0


def relax(u, v, key = 'vecinos'):
    new_dist = u['distancia'] + u[key][v['name']]
    if v['distancia'] > new_dist:
        v['distancia'] = new_dist
        v['predecesor'] = u['name']
```