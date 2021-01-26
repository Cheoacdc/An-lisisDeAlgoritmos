# Códigos de Hoffman
## Descripción:
Dadas ciertas letras de algún texto, se busca asginar un número binario a cada una, pero de manera que aquellas que se repiten mucho puedan ser representadas con la menor cantidad de dígitos posible, para ahorrar espacio.
* Input: Un **conjunto** de letras con su número de repeticiones.
* Output: Un arreglo que indica el código binario a asignarle a cada letra.

## Código utilizado:
### Función **Hoffman**
Con esta función se construye el árbol binario, con donde a cada letra se le asigna una hoja.
```python
def hoffman(conjunto):
    merge_sort_dict(conjunto)
    n = len(conjunto) - 1
    aux = [q for q in conjunto]
    for i in range(n):
        z = {}
        z['left'] = x = aux.pop(0)
        z['right'] = y = aux.pop(0)
        z['value'] = x['value'] + y['value']
        ordered_insert(aux, z)
    return aux.pop(0)


def ordered_insert(arr, node):
    arr.append(node)
    merge_sort_dict(arr)
```

### Construyendo la respuesta:
Con estas funciones se asigna el código binario a cada hoja, **Build Answer** regresa el arreglo con las letras y sus números binarios asignados.
```python
def build_answer(root):
    arr = []
    add_nodes(arr, root['left'], '0')
    add_nodes(arr, root['right'], '1')
    merge_sort_dict(arr, key='code', conversion=True)
    return arr


def add_nodes(arr, nodo, code):
    if is_leaf(nodo):
        arr.append({'letter': nodo['letter'], 'code': code})
    else:
        if nodo.get('left', None):
            add_nodes(arr, nodo.get('left'), code + '0')
        if nodo.get('right', None):
            add_nodes(arr, nodo.get('right'), code + '1')


def is_leaf(nodo):
    return not (nodo.get('left', None) and nodo.get('right', None))
```
