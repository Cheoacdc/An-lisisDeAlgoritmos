# Merge Sort

## Descripción:
Es uno de los algoritmos basados en la idea de *divide y vencerás*, que consiste en dividir el problema en subproblemas más pequeños y manejables, para resolver el problema original de menos a más.
* Input:
    * **arr**: Un arreglo de *n* números.
    * **p**: El índice del primer elemento del arreglo a ordenar
    * **r**: El índice del último elemento del arreglo a ordenar
* Output: Una permutación de dicha secuencia ordenada ascendentemente.
* Tiempo de ejecución: theta(nlgn)
    * Dado que siempre realiza todo el proceso sin importar el orden del arreglo, siempre se tiene un tiempo de ejecución *nlgn*.

## Código utilizado:
### Función **Merge**
Esta función se encarga de realizar la combinación de dos arreglos ordenados, resultando en un arreglo que contiene los elementos ordenados de los arreglos previos.
```python
def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    l_arr = []
    r_arr = []
    for i in range(n1):
        l_arr.append(arr[p + i])
    for j in range(n2):
        r_arr.append(arr[q + j + 1])
    l_arr.append(np.inf)
    r_arr.append(np.inf)
    i = j = 0
    for k in range(p, r + 1):
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
```

### Función **Merge-Sort**
Esta función se encarga de realizar la subdivisión de problemas, para luego conseguir la solución apoyándose de la función **Merge**.
```python
def merge_sort(arr, p, r):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = math.floor((p + r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
```