# Quicksort

## Descripción:
Es uno de los algoritmos basados en la idea de *divide y vencerás*, que consiste en dividir el problema en subproblemas más pequeños y manejables, pero a diferencia de **Merge-Sort**, se resuelve mientras se crean las divisiones. Otra punto importante es que **Merge-Sort** siempre es *nlgn* sin importar el arreglo, cuando **Quicksort** cambia. En promedio puede ser más rápido, pero en el peor de los casos se vuelve cuadrático.
* Input:
    * **arr**: Un arreglo de *n* números.
    * **p**: El índice del primer elemento del arreglo a ordenar.
    * **r**: El índice del último elemento del arreglo a ordenar.
* Output: Una permutación de dicha secuencia ordenada ascendentemente.
* Tiempo de ejecución: el peor de los casos es theta(n^2), sin embargo en la práctica, el promedio es *nlgn*.

## Código utilizado:
### Función **Partition**
Esta función divide al arreglo a partir de un elemento *r*, poniendo todos los elementos menores a éste a su izquierda y los mayores a su derecha, de esta forma se asigna el lugar correcto al elemento *r*.
```python
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

### Función **Quicksort**
Esta función se encarga de realizar la subdivisión de problemas apoyándose de la función **Partition**. Después itera sobre los dos subarreglos generados hasta que el problema no se pueda dividir más, para entonces el arreglo completo ya estará ordenado.
```python
def quicksort(arr, p, r):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
```