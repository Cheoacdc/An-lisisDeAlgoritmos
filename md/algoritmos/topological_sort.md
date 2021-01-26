# Topological Sort

## Descripción:
* Input: Una gráfica **G** representada como lista de adyacencia.
* Output: Se muestran los nodos de la gráfica en orden topológico.
* Tiempo de ejecución: O(V + E).
## Código utilizado:
Esta función se apoya de la función **DFS** para asignar el orden a los nodos.
```python
def topological_sort(graph):
    dfs(graph)
    ordered = [v for v in graph]
    merge_sort_dict(ordered, key='f')
    result = []
    for v in ordered:
        aux = [v.get('name', graph.index(v))]
        aux.extend(result)
        result = aux
    print(result)
```