# Binary Search Max

## Descripción:
Versión de binary search que, en caso de no encontrar el valor en el arreglo, devuelve el índice del elemento que máximo con respecto a éste.
* Input:
    * **arr**: Un arreglo de *n* números ordenados ascendentemente.
    * **x**: El valor del elemento a encontrar.
    * **i**: El índice a partir del cuál se realizará la búsqueda.
    * **j**: El índice a partir del cuál se realizará la búsqueda.
* Output: Índice del valor que se buscó, en caso de no encontrarlo, regresa el índice del elemento máximo con respecto a éste.
* Tiempo de ejecución: O(lgn).

## Código utilizado:
### Función **Binary Search Max**
El parámetro *best* tiene default de 0, pero una vez que inicia la ejecución se utiliza para guardar el índice del elemento que se acerque más al valor, sin ser mayor que éste, evidentemente.
```python
def binary_search_m(arr, x, i, j, best = 0):
    m = math.ceil((i + j - 1)/2)
    if x == arr[m]:
        return m
    elif (x - arr[m] > 0) and (x - arr[m] < x - arr[best]):
        best = m
    if x < arr[m]:
        if not i < m:
            if arr[best] > x:
                return None
            return best
        return binary_search_m(arr, x, i, m - 1, best)
    else:
        if not j > m:
            return best
        return binary_search_m(arr, x, m + 1, j, best)
```