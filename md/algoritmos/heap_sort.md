# Heap Sort

## Descripción:
Este algoritmo utiliza una estructura llamada Max Heap, que es básicamente un árbol binario donde el nodo padre siempre es mayor que sus dos nodos hijos.
* Input: Un arreglo **arr** de *n* números.
* Output: Una permutación de dicha secuencia ordenada ascendentemente.
* Tiempo de ejecución: O(nlgn)

## Código utilizado:
### Funciones de apoyo
Estas funciones nos permiten encontrar el índice que tendría cierto elemento en el heap.
```python
def left_of(i: int) -> int:
    return 2*(i + 1) - 1

def right_of(i: int) -> int:
    return 2 * (i + 1)
```

### Función **Max Heapify**
Esta función se encarga de darle estructura de Max Heap al arreglo a partir del índice *i*.
```python
def max_heapify(arr: List, i: int, heapsize: int) -> None:
    left = left_of(i)
    right = right_of(i)
    largest = left if left <= heapsize and arr[left] > arr[i] else i
    largest = right if right <= heapsize and arr[right] > arr[largest] else largest
    if not largest == i:
        exchange(arr, i, largest)
        max_heapify(arr, largest, heapsize)
```

### Función **Build Max Heap**
Con esta función se le da estructura de Max Heap a todo el arreglo, apoyándose de la función **Max Heapify**.
```python
def build_max_heap(arr: List) -> int:
    heapsize = len(arr) - 1
    i = math.floor(heapsize/2)
    while i >= 0:
        max_heapify(arr, i, heapsize)
        i -= 1
    return heapsize
```
### Función **Heap Sort**
Una vez que se convierte el arreglo en un Max Heap, comienza el ordenamiento en orden descendiente.
```python
def heap_sort(arr: List) -> None:
    heapsize = build_max_heap(arr)
    while heapsize > 0:
        exchange(arr, 0, heapsize)
        heapsize -= 1
        max_heapify(arr, 0, heapsize)
```