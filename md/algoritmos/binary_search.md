# Binary Search

## Descripción:
Algoritmo de búsqueda que, a partir de un arreglo ordenado, encuentra el índice del valor que se busca.
* Input:
    * **arr**: Un arreglo de *n* números ordenados ascendentemente.
    * **x**: El valor del elemento a encontrar.
    * **i**: El índice a partir del cuál se realizará la búsqueda.
    * **j**: El índice a partir del cuál se realizará la búsqueda.
* Output: Índice del valor que se buscó, en caso de no encontrarlo, regresa Null.
* Tiempo de ejecución: O(lgn).

## Código utilizado:
### Función **Binary Search**
Esta es la versión recursiva de binary search.
```python
def binary_search_r(arr, x, i, j):
    m = math.ceil((i + j - 1)/2)
    if x == arr[m]:
        return m
    elif x < arr[m] and i < m:
        return binary_search_r(arr, x, i, m - 1)
    elif x > arr[m] and j > m:
        return binary_search_r(arr, x, m + 1, j)
    else:
        return None
```