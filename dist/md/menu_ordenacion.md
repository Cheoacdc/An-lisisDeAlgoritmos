# Algortimos de búsqueda y ordenación

Dado que algunos algoritmos de búsqueda requieren de tener un arreglo ordenado, si se ejecuta un algoritmo de ordenación
se guardará la versión original y la versión ordenada. De esta manera no se tendrá que reordenar cada que se utilice un 
algoritmo de búsqueda y también se podrá ordenar el mismo arreglo utilizando los demás métdos de ordenación. En caso de 
ser requerido pero no se ha ordenado previamente, se utilizará Merge-sort debido a su tiempo de ejecución. 

### Lista de algoritmos
1. Insertion-sort
2. Merge-sort
3. Heap-sort
4. Quicksort
5. Randomized Quicksort
6. Counting-sort
7. Linear Search
8. Binary Search
9. Binary Search (Max)
    * Modificación de binary search, que en caso de no encontrar el número buscado, se devuelve el elemento máximo
    en el arreglo con respecto a dicho número.
10. Encuentra Suma 
    * Algoritmo que, dado un número, encuentra el par de números dentro de un arreglo cuya suma sea la
    máxima respecto a dicho número.

#### Nota
Para poder observar las diferencias en tiempos de ejecución, se ejecutarán 100000 veces los algoritmos.
De esta forma es posible mostrar la barra de progreso para cada uno de los algoritmos.  