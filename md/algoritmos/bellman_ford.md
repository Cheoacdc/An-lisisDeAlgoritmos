# Bellman Ford

## Descripción:
Con este algoritmo se busca la menor distancia a todos los nodos desde cierto nodo. También se asignan predecesores a cada uno para poder construir el camino más corto.
Este algoritmo, a diferencia de **Dijkstra**, permite pesos negativos en las aristas de la gráfica.
* Input:
    * **graph**: Una gráfica representada como lista de adyacencia.
    * **source**: El nodo a partir del cual se asignarán las distancias.
* Output: La gráfica con las distancias desde *source* a cada nodo.
* Tiempo de ejecución: O(VE)
## Código utilizado:
### Función Bellman-Ford
Esta es la función principal del algoritmo. Se apoya de dos funciones que comparte con el algoritmo **Dijkstra**.
```python
def bellman_ford(graph, source):
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