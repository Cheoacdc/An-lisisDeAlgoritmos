# Insertion Sort

## Descripción:
* Input: Una secuencia *A* de *n* números.
* Output: Una permutación de dicha secuencia ordenada ascendentemente.
* Tiempo de ejecución: O(n^2)

## Código utilizado:
```python
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
```