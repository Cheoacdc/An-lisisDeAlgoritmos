# Activity Selector
## Descripción:
Este algoritmo permite escoger la mayor cantidad de actividades sin que se empalmen.
* Input: Arreglo **arr** de *n* actividades, cada una con inicio y final, ordenadas de acuerdo a las horas de finalización.
* Output: Arreglo con las actividades seleccionadas.
* Tiempo de ejecución: theta(m), siendo m el total de actividades seleccionadas, sin embargo es evidente que m es a lo mucho n, por lo que el tiempo es theta(n).

## Código utilizado:
Esta es la versión que se utiliza para la ejecución del programa, la versión original no cuenta con un ordenamiento. Se decidió utilizar una variante de **Merge Sort** que pueda ordenar un arreglo de objetos para que el usuario pueda meter los elementos en desorden sin que el algoritmo deje de funcionar.
```python
def greedy_activity_selector(arr):
    merge_sort_dict(arr, key='end')
    k = 0
    result = [arr[k]]
    for m in range(1, len(arr)):
        if arr[m]['start'] >= arr[k]['end']:
            result.append(arr[m])
            k = m
    return result
```