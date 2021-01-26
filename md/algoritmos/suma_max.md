# Encuentra Suma Max

## Descripción:
Este algoritmo fue el resultado de un problema del libro mencionado en la bibliografía.
Encuentra el par de elementos cuya suma sea máxima dado un valor y.
* Input:
    * **arr**: Un arreglo de *n* números ordenados ascendentemente.
    * **y**: El valor que debe satisfacer la suma de dos elementos del arreglo.
* Output: Se regresa una tupla, con los valores de los dos elementos cuyos valores sumados es el máximo con respecto a y.
* Tiempo de ejecución: O(nlgn).

## Código utilizado:
### Función **Encuentra Suma Max**
Ésta función se apoya de **Binary Search Max** para encontrar elementos máximos en caso de que no se llegue al resultado exacto.
```python
def encuentra_suma_max(A, y):
    bxi = -np.inf
    bxj = -np.inf
    for j in range(len(A)):
        i = binary_search_m(A, abs(y - A[j]), 0, len(A) - 1, 0)
        if i is None:
            continue
        if (A[i] + A[j] > bxi + bxj) and (A[i] + A[j] <= y):
            bxi = A[i]
            bxj = A[j]
        if bxi + bxj == y:
            break
    return bxi, bxj
```