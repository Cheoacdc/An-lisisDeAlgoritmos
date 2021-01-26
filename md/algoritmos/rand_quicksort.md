# Quicksort

## Descripción:
Es una variación de **Quicksort**, sin embargo, se considera que esta versión es, en promedio, más eficiente. Esto se debe que al tomar de manera aleatoria el elemento a partir del cual se realiza la partición, si se ingresa un arreglo con ordeado (ya sea ascendente o descendentemente), no se realice el proceso, ya que se haría en tiempo cuadrático.
* Input:
    * **arr**: Un arreglo de *n* números.
    * **p**: El índice del primer elemento del arreglo a ordenar.
    * **r**: El índice del último elemento del arreglo a ordenar.
* Output: Una permutación de dicha secuencia ordenada ascendentemente.
* Tiempo de ejecución: el peor de los casos es theta(n^2), sin embargo en la práctica, el promedio es *nlgn*.

## Código utilizado:
### Función **Randomized Partition**
Lo especial de esta función es que antes de realizar la partición, cambia el último elemento por alguno diferente dentro del rango establecido, para evitar llegar trabajar con el peor de los casos.
```python
def randomized_partition(arr: List, p: int, r: int) -> int:
    i = random.randint(p, r)
    exchange(arr, r, i)
    return partition(arr, p, r)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            exchange(arr, i, j)
    exchange(arr, i + 1, r)
    return i + 1
```

### Función **Randomized Quicksort**
Prácticamente lo mismo que quicksort, pero se llama **Randomized Partition** en lugar de **Partition**.
```python
def randomized_quicksort(arr: List, p: int = 0, r: int = None) -> None:
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
```