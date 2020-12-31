from typing import List, Dict

from ordenacion.merge_sort import merge_sort_dict


def hoffman(conjunto: List[Dict]):
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


def ordered_insert(arr: List[Dict], node: Dict):
    arr.append(node)
    merge_sort_dict(arr)


def build_answer(root: Dict):
    arr = []
    add_nodes(arr, root['left'], '0')
    add_nodes(arr, root['right'], '1')
    merge_sort_dict(arr, key='code', conversion=True)
    return arr


def add_nodes(arr: List, nodo: Dict, code: str):
    if is_leaf(nodo):
        arr.append({'letter': nodo['letter'], 'code': code})
    else:
        if nodo.get('left', None):
            add_nodes(arr, nodo.get('left'), code + '0')
        if nodo.get('right', None):
            add_nodes(arr, nodo.get('right'), code + '1')


def is_leaf(nodo: Dict):
    return not (nodo.get('left', None) and nodo.get('right', None))
