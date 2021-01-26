# Orden de multiplicación de matrices

## Descripción:
El proceso de multiplicación de matrices puede ser muy ineficiente si no se colocan correctamente los paréntesis para realizar la operación.
Este algoritmo se encarga de encontrar la mejor configuración de paréntesis para multiplicar una serie de matrices.
* Input: Un arreglo **dims** donde se indiquen las dimensiones de las matrices a multiplicar.
* Output: La función **Matrix Chain Order** devuelve los arreglos auxiliares de costo y de índices, sin embargo, con la función **Build Optimal Parenthesis** se muestra la mejor configuración ya sea para todas las matrices o sólo para cierta sucesión de matrices del arreglo.

## Código utilizado:
```python
def matrix_chain_order(dims):
    n = len(dims) - 1
    costs = np.zeros((n, n))
    indices = np.zeros((n, n), dtype=int)
    for l in range(1, n):
        for i in range(0, n - l):
            j = i + l
            costs[i, j] = np.inf
            for k in range(i, j):
                q = costs[i, k] + costs[k + 1, j] + dims[i]*dims[k + 1]*dims[j + 1]
                if q < costs[i, j]:
                    costs[i, j] = q
                    indices[i, j] = k
    return costs, indices


def build_optimal_parenthesis(s, i, j):
    sol = ''
    if i == j:
        sol += f'A{i + 1}'
    else:
        sol += '('
        sol += build_optimal_parenthesis(s, i, s[i, j])
        sol += build_optimal_parenthesis(s, s[i, j] + 1, j)
        sol += ')'
    return sol
```