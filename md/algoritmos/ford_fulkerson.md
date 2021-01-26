# Ford Fulkerson

## Descripción:
Este algoritmo busca el flujo máximo que puede tener una gráfica. La gráfica debe tener un nodo *source*, del cual sólo sale flujo, y un nodo *well*, del cual sólo entra flujo. No se permiten flujos negativos, en caso de tener un flujo *f* negativo de *u* a *v*, se puede representar como *|f|* de *v* a *u*.
* Input: Una gráfica  **graph** representada como lista de adyacencia.
* Output: La gráfica con los flujos desde *source* a cada nodo. Para conocer el flujo máximo basta con sumar los flujos que recibe el nodo **well**.
* Tiempo de ejecución: La implementación en este programa es de O(F(V(V + lgV))), sin embargo con Fibonacci Heaps se puede conseguir un tiempo de O(F(VlgV + E)). Esto se debe a que se utiliza **Dijkstra** dependiendo del número de aristas del flujo.
## Código utilizado:
### Función **Ford Fulkerson**
Esta es la función principal del algoritmo. Se apoya de dos funciones que comparte con el algoritmo **Bellman Ford**. Además, se utiliza **Binary Search** para evitar reordenar por completo la *queue*.
```python
def ford_fulkerson(graph):
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
```
### Función **Get Shortest Path**
Aquí se utiliza una versión modificada de **Dikstra**, además que se va calculando la capacidad mínima del camino mientras se encuentra el camino, para evitar recorrerlo varias veces.
```python
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
```
### Función **Modified Dijkstra**
Se adaptó **Dijkstra** para ajustarse a las necesidades del problema, sin embargo son modificaciones menores, como que siempre se parte del nodo *source* y el nombre de las *keys* en las que se buscan los vecinos, en este caso es *capacidades*. Esto último es más relevante para el lenguaje de programación que para el algoritmo mismo.
```python
def modified_dijkstra(graph):
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
```
