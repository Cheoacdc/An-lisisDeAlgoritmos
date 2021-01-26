# Counting Sort

## Descripción:
Este es el primero de los algoritmos capaces de ordenar en tiempo lineal. Sin embargo, es necesario tener información previa sobre el arreglo. Se debe conocer el valor del elemento máximo de éste. También depende que el valor máximo sea lineal en comparación a *n*, ya que si es mucho mayor, el tiempo de ejecución se verá afectado.
* Input:
    * **arr**: Un arreglo de *n* números.
    * **k**: El valor del elemento máximo del arreglo.
* Output: Una permutación de dicha secuencia ordenada ascendentemente.
* Tiempo de ejecución: O(k + n), si k = O(n) => el tiempo de ejecución es O(n)

##### Nota:
Si se ingresan valores menores a cero, o si durante la ejecución del programa no se brinda el valor máximo del arreglo, no se podrá correr adecuadamente. Favor de ingresar los datos correctamente.

## Código utilizado:
### Counting Sort
Utilizando el valor máximo del arreglo, este algoritmo es capaz de utilizar un arreglo auxiliar para contar el número de repeticiones de cada número entre 0 y k, logrando un tiempo lineal, si k es lineal.
```python
def counting_sort(arr, k):
    snapshot_arr = [n for n in arr]
    aux_arr = np.zeros(k + 1, np.int)
    for j in range(len(arr)):
        aux_arr[arr[j]] += 1
    for i in range(1, k + 1):
        aux_arr[i] = aux_arr[i] + aux_arr[i - 1]
    j = len(arr) - 1
    while j >= 0:
        aux_arr[snapshot_arr[j]] -= 1
        arr[aux_arr[snapshot_arr[j]]] = snapshot_arr[j]
        j -= 1
```