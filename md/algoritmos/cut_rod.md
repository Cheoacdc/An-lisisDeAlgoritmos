# Cortado de Varillas

## Descripción:
Se sabe el precio al que se debe de vender una varilla de cierta la longitud. El algoritmo encuentra la mayor ganancia ya la forma óptima de cortar varillas de diferentes longitudes.
Se utilizan dos arreglos auxiliares, uno para guarder el corte óptimo y el otro para guardar el precio de dicho corte.
* Input:
    * **p**: Arreglo que indica el precio al realizar un corte de cierta longitud.
    * **n**: La longitud para la cuál se quiere encontrar el corte óptimo.
    * **r**: Arreglo auxiliar para guardar los cortes óptimos.
    * **s**: Arreglo auxiliar para guardar los precios.
* Output: Regresa tanto el precio como un arreglo que indica cómo se deben realizar los cortes.

## Código utilizado:
```python
def extended_buttom_up_cut_rod(p, n, r, s):
    for j in range(1, n + 1):
        q = -np.inf
        if r[j] == 0:
            for i in range(1, j + 1):
                if q <= p[i] + r[j - i]:
                    q = p[i] + r[j - i]
                    s[j] = i
            r[j] = q


def build_cut_rod_solution(p, n, r, s):
    if not r or not len(r) == len(p):
        r = np.zeros(len(p))
    if not s or not len(s) == len(p):
        s = np.zeros(len(p), dtype=int)
    extended_buttom_up_cut_rod(p, n, r, s)
    price = r[n]
    cuts = []
    while n > 0:
        cuts.append(s[n])
        n -= s[n]
    return price, cuts
```