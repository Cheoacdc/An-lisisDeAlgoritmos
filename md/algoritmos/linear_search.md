# Linear Search

## Descripción:
* Input:
    * **A**: Arreglo de *n* números.
    * **v**: Valor a encontrar en el arreglo.
* Output: Índice del valor que se buscó, en caso de no encontrarlo, regresa Null.
* Tiempo de ejecución: O(n), pero el promedio es *n/2*, aunque sigue siendo lineal finalmente.

## Código utilizado:
```python
def linear_search(A, v):
    for j in range(len(A)):
        if A[j] == v:
            return j
        else:
            j += 1
```