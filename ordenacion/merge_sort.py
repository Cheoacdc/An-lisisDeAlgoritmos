import math
import numpy as np

from typing import Dict, List


def merge(arr: List, p: int, q: int, r: int) -> None:
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


def merge_sort(arr: List, p: int = 0, r: int = None):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = math.floor((p + r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge_dict(arr: List[Dict], p: int, q: int, r: int, key: str = 'value', conversion: bool = False) -> None:
    n1 = q - p + 1
    n2 = r - q
    l_arr = []
    r_arr = []

    def fun(x):
        return float(x) if conversion else x
    for i in range(n1):
        l_arr.append(arr[p + i])
    for j in range(n2):
        r_arr.append(arr[q + j + 1])
    inf_dict = {key: np.inf}
    l_arr.append(inf_dict)
    r_arr.append(inf_dict)
    i = j = 0
    for k in range(p, r + 1):
        if fun(l_arr[i][key]) <= fun(r_arr[j][key]):
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1


def merge_sort_dict(arr: List[Dict], p: int = 0, r: int = None, key: str = 'value', conversion: bool = False):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = math.floor((p + r)/2)
        merge_sort_dict(arr, p, q, key, conversion)
        merge_sort_dict(arr, q + 1, r, key, conversion)
        merge_dict(arr, p, q, r, key, conversion)
